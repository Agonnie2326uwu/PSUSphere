<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Organization, OrgMember, Student, College, Program
from .forms import (
    OrganizationForm,
    OrgMemberForm,
    StudentForm,
    CollegeForm,
    ProgramForm,
)

# ✅ Homepage
class HomePageView(TemplateView):
    template_name = "home.html"


# ✅ Organization Views
class OrganizationList(ListView):
    model = Organization
    template_name = "organization/list.html"
    context_object_name = "organizations"
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "organization/form.html"
    success_url = reverse_lazy("organization-list")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "organization/form.html"
    success_url = reverse_lazy("organization-list")

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "organization/del.html"
    success_url = reverse_lazy("organization-list")


# ✅ OrgMember Views
class OrgMemberList(ListView):
    model = OrgMember
    template_name = "orgmember/list.html"
    context_object_name = "orgmembers"
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember/form.html"
    success_url = reverse_lazy("orgmember-list")

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember/form.html"
    success_url = reverse_lazy("orgmember-list")

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "orgmember/del.html"
    success_url = reverse_lazy("orgmember-list")


# ✅ Student Views
class StudentList(ListView):
    model = Student
    template_name = "student/list.html"
    context_object_name = "students"
    paginate_by = 5

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/form.html"
    success_url = reverse_lazy("student-list")

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student/form.html"
    success_url = reverse_lazy("student-list")

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student/del.html"
    success_url = reverse_lazy("student-list")


# ✅ College Views
class CollegeList(ListView):
    model = College
    template_name = "college/list.html"
    context_object_name = "colleges"
    paginate_by = 5

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college/form.html"
    success_url = reverse_lazy("college-list")

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college/form.html"
    success_url = reverse_lazy("college-list")

class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college/del.html"
    success_url = reverse_lazy("college-list")


# ✅ Program Views
class ProgramList(ListView):
    model = Program
    template_name = "program/list.html"
    context_object_name = "programs"
    paginate_by = 5

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program/form.html"
    success_url = reverse_lazy("program-list")

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program/form.html"
    success_url = reverse_lazy("program-list")

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "program/del.html"
    success_url = reverse_lazy("program-list")
>>>>>>> Stashed changes
