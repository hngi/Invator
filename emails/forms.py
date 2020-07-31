from django import forms
from django.forms import ClearableFileInput
from .models import Emails
from django.core.exceptions import ValidationError


class EmailsForm(forms.ModelForm):
	name = forms.CharField(label="Your Name:", max_length=254,
					widget=forms.TextInput(
					attrs={
						'placeholder': 'Enter your name',
						'class': 'form-control',
					})
				)
	message = forms.CharField(label="Your Message:", max_length=2000,
					widget=forms.Textarea(
					attrs={
						'placeholder': 'Enter your message',
						'class': 'form-control',
						'rows': 50,
						'cols': 70,
					})
				)
	sender = forms.EmailField(
					widget=forms.TextInput(
					attrs={
						'placeholder': 'Enter your email address',
						'class': 'form-control',
					})
				)

	recipient = forms.EmailField(
					widget=forms.TextInput(
					attrs={
						'placeholder': 'Enter email address of recipient',
						'class': 'form-control',
					})
				)
	attach = forms.FileField(
					widget=ClearableFileInput(
					attrs={
						'multiple': True,
					}))

	class Meta:
		model = Emails
		fields = [
			'name',
			'message',
			'sender',
			'recipient',
			'attach'
		]


	def clean_recipient(self, *args, **kwargs):
		recipient = self.cleaned_data.get('recipient')
		if not "@" in recipient:
			raise ValidationError("This is not a valid email address.")
		return recipient