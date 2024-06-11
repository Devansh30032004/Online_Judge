from django.contrib import admin # type: ignore
from .models import Problem, TestCase, Submission, CodeSubmission, Profile
from django.utils.html import format_html
from .forms import ProblemForm, TestCaseForm, SubmissionForm, CodeSubmissionForm, ProfilePictureForm
from .views import view_code1
from django.urls import path
from django.contrib import admin

class ProblemAdmin(admin.ModelAdmin):
    form = ProblemForm

class TestCaseAdmin(admin.ModelAdmin):
    form = TestCaseForm

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'language', 'time_taken', 'memory_used', 'verdict', 'submission_time', 'view_code_link')
    search_fields = ('user__username', 'problem__title', 'verdict')
    list_filter = ('language', 'verdict', 'submission_time')
    readonly_fields = ('submission_time',)

    def view_code_link(self, obj):
        return format_html('<a href="{}">View Code</a>', f'view_code/{obj.id}/')

    view_code_link.short_description = 'View Code'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('view_code/<int:id>/', self.admin_site.admin_view(view_code1), name='view_code1'),
        ]
        return custom_urls + urls
    
class ProfileAdmin(admin.ModelAdmin):
    form = ProfilePictureForm


admin.site.register(Problem, ProblemAdmin)
admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Profile, ProfileAdmin)