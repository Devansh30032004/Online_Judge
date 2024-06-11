from django import forms
from .models import Problem, TestCase, Submission, CodeSubmission, Profile
import json

class JSONInputField(forms.CharField):
    def prepare_value(self, value):
        if isinstance(value, list):
            return json.dumps(value, indent=2)
        return value

    def to_python(self, value):
        if not value:
            return []
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            raise forms.ValidationError("Invalid JSON format. Please enter a valid JSON array.")

class ProblemForm(forms.ModelForm):
    base_inputs = JSONInputField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))
    base_outputs = JSONInputField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Problem
        fields = '__all__'

class TestCaseForm(forms.ModelForm):
    input_data = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))
    expected_output = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = TestCase
        fields = '__all__'

class SubmissionForm(forms.ModelForm):
    LANGUAGE_CHOICES = [
        ('c', 'C'),
        ('cpp', 'C++'),
        ('python', 'Python'),
    ]

    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

    class Meta:
        model = Submission
        fields = ['language', 'code']

class CodeSubmissionForm(forms.ModelForm):
    LANGUAGE_CHOICES = [
        ('c', 'C'),
        ('cpp', 'C++'),
        ('python', 'Python'),
    ]
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

    class Meta:
        model = CodeSubmission
        fields = ["language", "code", "input_data"]

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','profile_picture',]