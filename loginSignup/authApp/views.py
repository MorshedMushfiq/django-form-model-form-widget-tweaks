from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth.models import User
from authApp.forms.login_form import LoginForm
from authApp.forms.register_form import Register_form
from authApp.forms.student_form import StudentForm

# Create your views here.

# register form using django forms
def register(req):
        register_form  = Register_form()

        if req.method == 'POST':
            username = req.POST.get('username')
            email = req.POST.get('email')
            password = req.POST.get('password')
            con_pass = req.POST.get('confirm_password')
            if not all([username, email, password, con_pass]):
                messages.warning(req, 'All Fields are Required')
                return render(req, 'register.html')
            try:
                validate_email(email)
            except ValidationError:
                messages.warning(req, "invalid email format") 
                return render(req, 'register.html')   
            if password != con_pass:
                messages.warning(req, 'Password and Confirm Password do not match')
                return render(req, 'register.html')
            try:
                user = User.objects.create_user(username=username, email=email, password=con_pass)
                messages.success(req,  'User Created Successfully')
                return redirect('loginPage')

            except IntegrityError:
                messages.warning(req, 'Username already exists')
                return render(req, 'register.html')
    
        return render(req, "register.html", {"r":register_form})


# login form using django forms
def loginPage(req):
        login_form = LoginForm()
        if req.method == "POST":
            username = req.POST.get('username')
            password = req.POST.get('password')
            if not all([username, password]):
                messages.warning(req,  'All Fields are Required')
                return render(req, 'login.html')
            else: 
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(req, user)
                    messages.success(req,  'Login Successful')
                    return redirect('home')
                else: 
                    messages.warning(req,  'Invalid Credentials')
                    return render(req, 'login.html')
        return render(req, "login.html", {'f':login_form})



# home page with login
@login_required
def home(req):
    return render(req, 'home.html')



# logout functionality
@login_required
def logoutPage(req):
    logout(req)
    messages.success(req, "Log Out Successful!!")
    return redirect('loginPage')


# add student functionality using django model form
@login_required
def add_student(req):
    # obviously you have to create an instance for the StudentForm() class. if you call inside the post you'll get error of unbound variable couldn't access student1 variable.
    # please create the instance(student1 = StudentForm()) before the if req.method == "POST":
    student1 = StudentForm()
    if req.method == "POST":
        student1 = StudentForm(req.POST)
        if student1.is_valid():
            student1.save()
            messages.success(req, "Student Add Success!!!")
            return redirect('home')
        else: 
            student1 = StudentForm()

    context = {
        's':student1
    }
    return render(req, "add_student.html", context)