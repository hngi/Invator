from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
	name = forms.CharField(label="Your Name:", max_length=254,
					widget=forms.TextInput(
					attrs={
						'placeholder': 'Your name',
						'class': 'form-control contact-input',
					}))
	email = forms.EmailField(label="Your Email:", max_length=254,
					widget=forms.TextInput(
					attrs={
						'placeholder': 'Your email address',
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


	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not "@" in email:
			raise ValidationError("This is not a valid email address.")
		return email