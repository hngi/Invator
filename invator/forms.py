from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(
					widget=forms.Textarea(
					attrs={
						'placeholder': 'Enter your message...',
						'class': 'form-control',
						'rows': 50,
						'cols': 70,
					})
				)

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not "@" in email:
			raise ValidationError("This is not a valid email address.")
		return email