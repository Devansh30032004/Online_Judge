from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore
from django.core.mail import EmailMessage, send_mail # type: ignore
from django.template import loader # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.conf import settings # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Problem, TestCase, Submission, CodeSubmission, Profile
from django.utils import timezone # type: ignore
from .forms import SubmissionForm, CodeSubmissionForm, ProfilePictureForm
import json
import subprocess
import time
import os
import uuid
from pathlib import Path
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView


# Create your views here.
def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "User with this username already exists!")
            return redirect('/register/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/register/')
        
        if len(username)>25:
            messages.error(request, "Username must be under 25 charcters!!")
            return redirect('/register/')
        
        user = User.objects.create_user(username = username,email = email)
        user.first_name = fname
        user.last_name = lname
        user.set_password(password)
        user.save()
        messages.info(request, "User created successfully..")

        # Send welcome email
        send_welcome_email(email, username)

        return redirect('home')
        
    return render(request, 'authentication/register.html')

def send_welcome_email(email, username):
    subject = 'Welcome to Online Judge'
    message = f'Hi {username},\n\nWelcome to Online Judge! We are excited to have you on board.\n\nHappy coding!\n\nBest Regards,\nOnline Judge Team'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        user = User.objects.filter(username = username)
        if not user.exists():
            messages.info(request, "Invalid username entered!")
            return redirect('/login/')
    
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request,"Invalid password !")
            return redirect('/login/')
    
        login(request, user)
        messages.info(request, "Logged in successfully..")
        return redirect('home')
    
    return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully..")
    return redirect('home')

def problem_list(request):
    problems = Problem.objects.all()
    template = loader.get_template('home/problem_list.html')
    context = {
        'problems': problems,
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from .models import Submission

def submission_list(request):
    page = request.GET.get('page', '1')  # Get page number from query params, default to '1'
    page = int(page) if page.isdigit() else 1  # Convert to int if it's a valid number, otherwise default to 1
    per_page = 10
    offset = (page - 1) * per_page
    limit = offset + per_page
    
    submissions = Submission.objects.all().order_by('-id')[offset:limit]
    total_submissions = Submission.objects.count()
    total_pages = (total_submissions + per_page - 1) // per_page  # Ceiling division
    
    context = {
        'submissions': submissions,
        'current_page': page,
        'total_pages': total_pages,
    }
    return render(request, 'home/submissions_list.html', context)


def home(request):
    return render(request,'home/home.html')

def problem_detail(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    base_io_pairs = zip(problem.base_inputs, problem.base_outputs)
    
    # Convert to JSON string if needed
    problem.base_inputs_json = json.dumps(problem.base_inputs)
    problem.base_outputs_json = json.dumps(problem.base_outputs)
    
    context = {
        'problem': problem,
        'base_io_pairs': base_io_pairs
    }
    return render(request, 'home/problem_detail.html', context)

@login_required
def submit_code(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.problem = problem
            submission.user = request.user  # Set the user
            submission.verdict, submission.time_taken, submission.memory_used = evaluate_code(request, submission)
            submission.save()
            return redirect('submission_detail', submission_id=submission.id)
    else:
        form = SubmissionForm()
    return render(request, 'home/submit.html', {'form': form, 'problem': problem})

def evaluate_code(request, submission):
    code = submission.code
    language = submission.language
    verdict = "Accepted"
    time_taken = 1  #in seconds
    memory_used = 0 # in KB
    testcases = TestCase.objects.filter(problem=submission.problem)
    path = settings.BASE_DIR
    files = ["codes", "inputs", "outputs"]
    for file in files:
        os.makedirs(path/file, exist_ok = True)

    # uuid version 4 generates unique O/P everytime and more secure than uuid1
    unique = str(uuid.uuid4())
    dict = {
        'cpp' : 'c++',
        'python' : 'py',
        'c' : 'c'
    }

    dict1 ={
        'cpp' : 'g++',
        'c' : 'gcc'
    }

    code_path = path / "codes"/ f'{unique}.{dict[language]}'
    output_path = path / "outputs"/ f'{unique}.txt'
    input_path = path / "inputs"/ f'{unique}.txt'


    with open(code_path, "w") as code_file:
        code_file.write(code)  
    
    if language == 'cpp' or language == 'c':
        executable_path = path / "codes" / unique
        compile_result = subprocess.run(
            [dict1[language], code_path, "-o", executable_path],
            capture_output= True,
            text = True
        )

        if compile_result.returncode:
            verdict = " Compilation Error !!\n" + f'{compile_result.stderr}'   
            return verdict, time_taken, memory_used
    cnt = 1
    for each_testcase in testcases:
        with open(input_path, "w") as f:
            f.write(each_testcase.input_data)
        with open(input_path, "r") as f:
            start_time = time.time()
            try:
                if language == 'cpp' or language == 'c':
                        run_result = subprocess.run(
                            [executable_path],
                            stdin=f,
                            text = True,
                            capture_output=True,
                            timeout=1
                        )
                else:
                    run_result = subprocess.run(
                        ["python3", code_path],
                        stdin=f,
                        text = True,
                        capture_output=True,
                        timeout=1
                    )
            except subprocess.TimeoutExpired:
                verdict = "Time Limit Exceeded !! More than one second"
                return verdict, time_taken, memory_used
            end_time = time.time()
            time_taken = end_time - start_time
            if run_result.returncode:
                verdict = " Runtime Error !!\n" + f'{run_result.stderr}' 
                return verdict, time_taken, memory_used
        
        with open(output_path, "w") as output_file:
            output_file.write(run_result.stdout)

        with open(output_path, "r") as output_file:
            yorker = output_file.read().splitlines()
        
        bouncer = [s for s in each_testcase.expected_output.split('\r\n') if s]
        if len(bouncer) != len(yorker):
            verdict = " Wrong Answer !\nOutput generated must have same format as described !"
            return verdict, time_taken, memory_used
        for tmp in range(len(bouncer)):
            yorker[tmp] = yorker[tmp].strip() 
            bouncer[tmp] = bouncer[tmp].strip() 
            if yorker[tmp] != bouncer[tmp]:
                verdict = f'Wrong answer at Testcase - {cnt} !' + "\n" + f'Expected : {bouncer[tmp]} but Found : {yorker[tmp]}'             
                return verdict, time_taken, memory_used
        cnt += 1

    return verdict, time_taken, memory_used

# This function should be placed outside any function, preferably at the top
def custom_login_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You need to be logged in to submit code.')
            return redirect('login')  # Redirect to the login page
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

# Now decorate the view with the custom login_required
@custom_login_required
def submit_code(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.problem = problem
            submission.user = request.user  # Set the user
            submission.verdict, submission.time_taken, submission.memory_used = evaluate_code(request, submission)
            submission.save()
            return redirect('submission_detail', submission_id=submission.id)
    else:
        form = SubmissionForm()
    return render(request, 'home/submit.html', {'form': form, 'problem': problem})

def run_code(request):
    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            language = form.cleaned_data['language']
            input_data = form.cleaned_data['input_data']
            output, time_taken, memory_used = execute_code(request, code, language, input_data)
            return render(request, 'home/run.html', {'form': form, 'output': output, 'time_taken': time_taken, 'memory_used': memory_used})
    else:
        form = CodeSubmissionForm()
    
    return render(request, 'home/run.html', {'form': form})

def execute_code(request, code, language, input_data):
    path = settings.BASE_DIR
    files = ["codes", "inputs", "outputs"]
    time_taken = 1 # in seconds
    memory_used = 0 # in KB
    output = ""

 # Define commands for each language
    dict = {
        'cpp' : 'c++',
        'python' : 'py',
        'c' : 'c'
    }

    dict1 ={
        'cpp' : 'g++',
        'c' : 'gcc'
    }

    for file in files:
        os.makedirs(path/file, exist_ok = True)
    
    unique = str(uuid.uuid4())
    code_path = path / "codes"/ f'{unique}.{dict[language]}'
    output_path = path / "outputs"/ f'{unique}.txt'
    input_path = path / "inputs"/ f'{unique}.txt'
    # Write code and input to files
    with open(code_path, 'w') as f:
        f.write(code)
    with open(input_path, 'w') as f:
        f.write(input_data)

    if language == 'cpp' or language == 'c':
        executable_path = path / "codes" / unique
        compile_result = subprocess.run(
            [dict1[language], code_path, "-o", executable_path],
            capture_output= True,
            text = True
        )

        if compile_result.returncode:
            output = " Compilation Error !!\n" + f'{compile_result.stderr}'   
            return output, time_taken, memory_used
        
    with open(input_path, "r") as f:
            start_time = time.time()
            try:
                if language == 'cpp' or language == 'c':
                        run_result = subprocess.run(
                            [executable_path],
                            stdin=f,
                            text = True,
                            capture_output=True,
                            timeout=1
                        )
                else:
                    run_result = subprocess.run(
                        ["python3", code_path],
                        stdin=f,
                        text = True,
                        capture_output=True,
                        timeout=1
                    )
            except subprocess.TimeoutExpired:
                output = "Time Limit Exceeded !! More than one second"
                return output, time_taken, memory_used
            end_time = time.time()
            time_taken = end_time - start_time
            if run_result.returncode:
                output = " Runtime Error !!\n" + f'{run_result.stderr}' 
                return output, time_taken, memory_used

    with open(output_path, "w") as output_file:
            output_file.write(run_result.stdout)

    with open(output_path, "r") as f:
        output = f.read()

    return output, time_taken, memory_used
    


def submission_detail(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, 'home/submission_detail.html', {'submission': submission})

@staff_member_required
def view_code1(request, id):
    obj = get_object_or_404(Submission, id=id)
    code = obj.code  # Assuming the model has a 'code' field

    return HttpResponse(f'<pre>{code}</pre>', content_type='text/html')

def view_code(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    return render(request, 'home/view_code.html', {'submission': submission})

@login_required
def profile(request):
    user = request.user

    # Ensure the Profile object exists for the user
    profile, created = Profile.objects.get_or_create(user=user)
    
    total_submissions = user.submission_set.count()
    correct_submissions = user.submission_set.filter(verdict='Accepted').count()
    wrong_submissions = total_submissions - correct_submissions
    accuracy = (correct_submissions / total_submissions * 100) if total_submissions > 0 else 0
    
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfilePictureForm(instance=profile)

    context = {
        'user': user,
        'profile': profile,
        'total_submissions': total_submissions,
        'correct_submissions': correct_submissions,
        'wrong_submissions': wrong_submissions,
        'accuracy': accuracy,
        'form': form,
    }
    
    return render(request, 'home/profile.html', context)
