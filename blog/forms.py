from django import forms

class MyForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(max_length=20, label="Phone Number")
    message = forms.CharField(widget=forms.Textarea, label="Message")
