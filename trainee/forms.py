from django import forms
from course.models import Course

class TraineeForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'})
    )
    course = forms.ChoiceField(
        choices=[(course.id, course.name) for course in Course.get_all_courses()],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
