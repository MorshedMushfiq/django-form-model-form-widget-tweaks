from django import forms
from authApp.models import StudentModel


# add student form using django model form
class StudentForm(forms.ModelForm):
    password = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput(attrs={"placeholder":  "Enter Password"}))

    class Meta:
        model = StudentModel
        fields = ['username', 'email', 'dept']
        