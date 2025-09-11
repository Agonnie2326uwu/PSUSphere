from django import forms
from .models import Organization, OrgMember, Student, College, Program

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'college', 'description']


class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = ['student', 'organization', 'date_joined']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'lastname', 'firstname', 'middlename', 'program']


class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['college_name']


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['prog_name', 'college']
