from django import forms



class SignForm(forms.Form):
	name = forms.CharField(max_length=20, widget=forms.TextInput())
	phone = forms.CharField(max_length=20, widget=forms.TextInput())
	email = forms.CharField(max_length=20, widget=forms.TextInput())