from django import forms
from django.forms import ClearableFileInput
from .models import Emails
from django.core.exceptions import ValidationError


class EmailsForm(forms.ModelForm):
	name = forms.CharField(label="Your Name:", max_length=254,
					widget=forms.TextInput(
					attrs={
						'placeholder': 'Your name',
						'class': 'form-control contact-input',
					})
				)
	message = forms.CharField(label="Your Message:", max_length=2000,
					widget=forms.Textarea(
					attrs={
						'placeholder': 'Your message',
						'class': 'form-control contact-msg',
						'rows': 10,
						'cols': 50,
					})
				)
	#sender = forms.EmailField(
	#				widget=forms.TextInput(
	#				attrs={
	#					'placeholder': 'Your email address',
	#					'class': 'form-control contact-input',
	#				})
	#			)

	recipient = forms.EmailField(
					widget=forms.TextInput(
					attrs={
						'placeholder': 'Email address of recipient',
						'class': 'form-control contact-input',
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
			#'sender',
			'recipient',
			'attach'
		]


	def clean_recipient(self, *args, **kwargs):
		recipient = self.cleaned_data.get('recipient')
		if not "@" in recipient:
			raise ValidationError("This is not a valid email address.")
		return recipient