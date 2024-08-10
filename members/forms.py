from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='First Name')
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Profile Image', required=False)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Phone Number', required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), label='Bio', required=False)
    joined_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), label='Date Joined')
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'email', 'joined_date', 'bio', 'profile_image', 'phone_number']
