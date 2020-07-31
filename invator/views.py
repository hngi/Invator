from django.shortcuts import render,redirect
#import weasyprint
from django.template.loader import render_to_string
#from weasyprint import HTML
import tempfile
from django.http import Http404, HttpResponse, JsonResponse
from .models import Invoice
from django.db.models import Sum, F
from datetime import datetime
from django.contrib import messages 
from django.contrib.auth import get_user_model

User = get_user_model()


def download_to_pdf(request, id):
    # pdf = weasyprint.HTML('http://127.0.0.1:8000').write_pdf()
    # new_file = file('google.pdf', 'wb').write(pdf)
    obj = Invoice.objects.get(id=id)
    data = obj.transactions.aggregate(sum = Sum(F('quantity') * F('price')))
    print(data)
    context = {"obj":obj, "sum":data["sum"]}
    html_string = render_to_string('preview_template_1.html', {'obj': obj})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(result, content_type='application/pdf')
    filename = "Invoice_%s.pdf" %(datetime.now())
    content = "inline; filename='%s'" %(filename)
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    response['Content-Transfer-Encoding'] = 'binary'

    return response

def preview_template(request, id):
    obj = Invoice.objects.get(id=id)
    data = obj.transactions.aggregate(sum = Sum(F('quantity') * F('price')))
    print(data, obj.tax)
    vat = int(data["sum"]) * float(obj.tax) / 100
    print(vat)
    total = int(data["sum"]) + vat
    context = {"obj":obj, "sum":data["sum"],"vat":vat, "total":total}
    return render(request, "preview_template_1.html", context)

from django.contrib.auth import get_user_model

User = get_user_model()

def dashboard(request):
    '''views for the dashboard template'''
    if request.user.is_authenticated:
        user = request.user
        #print(user)
        # if user.is_anonymous:
        #     pass
        # if user.is_authenticated:
        auth_invoice = Invoice.objects.filter(user=user)
        # show the latest invoices
        order_invoice = auth_invoice.order_by("-time")
        # only show 4 invoices at a time
        context = order_invoice[:4]
        if request.method == "POST":
            fullname = request.POST['fullname']
            username = request.POST['username']
            password = request.POST['password']
            job_type = request.POST['job_type']
            email = request.POST["email"]
            other_user = User.objects.exclude(id = request.user.id)
            if other_user.filter(username=username).exists():
                error = 'username already taken.'
                return render(request, 'dashboard.html',{'error':error})
            elif password == "":
                error = 'password should not be blank'
                return render(request, 'dashboard.html',{'error':error})
            elif User.objects.filter(username=username).exists():
                user.username = username
                user.first_name = fullname
                user.set_password(password)
                user.email = email
                user.save()
                print(password,username,email)
                userp = User.objects.get(email=email)
                userp.profile.job_type = job_type
                userp.save()
                          
        return render(request, "dashboard.html", {'data': context})

    return redirect("/login")