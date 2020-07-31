from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage, BadHeaderError
from django.contrib.auth.decorators import login_required
#from sendgrid import SendGridAPIClient
#from sendgrid.helpers.mail import *
#from root.settings import SENDGRID_API_KEY
from django.conf import settings
from .models import Emails
from .forms import EmailsForm

#@login_required
def email_invoice(request):
	form = EmailsForm()
	if request.method == "POST":
		form = EmailsForm(request.POST, request.FILES)
		if form.is_valid():
			print("Form works!")
			subject = f'Message from {form.cleaned_data["name"]}'
			message = form.cleaned_data["message"]
			sender = form.cleaned_data["sender"]
			recipient = form.cleaned_data["recipient"]
			files = request.FILES.getlist("attach")
			try:
				mail = EmailMessage(subject, message, sender, [recipient])
				for f in files:
					mail.attach(f.name, f.read(), f.content_type)
				mail.send()
				#sg = SendGridAPIClient(api_key=SENDGRID_API_KEY)
				#sg.send(mail.send())
			except BadHeaderError:
				return HttpResponse("Invalid header found!")
			return render(request, "")
	return render(request, "email-invoice.html", {'form': form})



