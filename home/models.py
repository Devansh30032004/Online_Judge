from django.db import models # type: ignore
import json
from django.contrib.auth.models import User # type: ignore

class Problem(models.Model):
    title = models.CharField(max_length=255, default='Default Title')
    description = models.TextField(default='Default Description')
    difficulty = models.CharField(max_length=10, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy')
    time_limit = models.FloatField(default=1.0)  # in seconds
    memory_limit = models.IntegerField(default=256)  # in KB
    constraints = models.TextField(default='Constraints go here')
    base_inputs = models.JSONField(default=list)  # stores list of base inputs
    base_outputs = models.JSONField(default=list)  # stores list of base outputs

    def __str__(self):
        return self.title

class TestCase(models.Model):
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, default='default')
    code = models.TextField()
    time_taken = models.FloatField()
    memory_used = models.FloatField(null=True, blank=True)
    verdict = models.CharField(max_length=20)
    submission_time = models.DateTimeField(auto_now_add=True)

class CodeSubmission(models.Model):
    language = models.CharField(max_length=100)
    code = models.TextField()
    time_taken = models.FloatField(default = 1.0)
    memory_used = models.FloatField(null=True, blank=True)
    input_data = models.TextField(null=True,blank=True)
    output_data = models.TextField(null=True, blank=True)
    submission_time = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
