from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'email', 'joined_date', 'bio']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'joined_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'slug': forms.HiddenInput()
        }
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email',
            'joined_date': 'Join Date',
            'bio': 'Bio',
            'slug': 'Slug'
        }