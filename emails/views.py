from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage, BadHeaderError
from django.contrib.auth.decorators import login_required
#from sendgrid import SendGridAPIClient
#from sendgrid.helpers.mail import *
#from root.settings import SENDGRID_API_KEY
from django.conf import settings
from .models import Emails
from django.contrib import messages
from .forms import EmailsForm

#@login_required
def email_invoice(request):
	form = EmailsForm()
	if request.method == "POST":
		form = EmailsForm(request.POST, request.FILES)
		if form.is_valid():
			subject = f'Message from {form.cleaned_data["name"]}'
			message = form.cleaned_data["message"]
			sender = settings.DEFAULT_FROM_EMAIL
			recipient = form.cleaned_data["recipient"]
			file = request.FILES["attach"]
			try:
				mail = EmailMessage(subject, message, sender, [recipient])
				mail.attach(file.name, file.read(), file.content_type)
				mail.send()
				messages.success(request, 'Invoice sent successfully!')
			except:
				messages.error(request, 'Invoice not sent!')
		
			return render(request, "email-invoice.html", {"form": form})
	return render(request, "email-invoice.html", {"form": form})



