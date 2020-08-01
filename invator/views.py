from django.shortcuts import render, redirect
import weasyprint
from django.template.loader import render_to_string
from weasyprint import HTML
from django.contrib.auth.decorators import login_required
import tempfile
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from .models import Invoice, Transaction
from django.db.models import Sum, F
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth import get_user_model
User = get_user_model()

def contact_page(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            try:
                send_mail(
                        name,
                        message,
                        email,
                        ["believemanasseh@gmail.com"],
                )
                messages.success(request, 'Message delivered successfully!')
            except BadHeaderError:
                messages.error(request, 'Message couldn\'t be delivered!') 
            return render(request, "contact.html", {"form": form})
    return render(request, "contact.html", {"form": form})
    
def homepage(request):
    return render(request, 'index.html')

def download_to_pdf(request, id):
    # pdf = weasyprint.HTML('http://127.0.0.1:8000').write_pdf()
    # new_file = file('google.pdf', 'wb').write(pdf)
    obj = Invoice.objects.get(id=id)
    data = obj.transactions.aggregate(sum = Sum(F('quantity') * F('price')))
    print(data, obj.tax)
    vat = int(data["sum"]) * float(obj.tax) / 100
    print(vat)
    total = int(data["sum"]) + vat
    context = {"obj":obj, "sum":data["sum"],"vat":vat, "total":total}
    html_string = render_to_string('02.html', context)
    html = HTML(string=html_string,
    base_url=request.build_absolute_uri())
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(result , content_type="application/pdf")
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
    count = Invoice.objects.filter(user=request.user).last().id + 1
    print(count)
    # count = obj_.id
    total = int(data["sum"]) + vat
    context = {"obj":obj, "sum":data["sum"],"vat":vat, "total":total, "count":count}
    return render(request, "preview_template_1.html", context)

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Invoice.objects.all().filter(id=search)
        return render(request, 'searchbar.html', {'post': post})

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
        '''
        li = []
        for i in order_invoice:
            data = i.transactions.aggregate(sum = Sum(F('quantity') * F('price')))
            print(data["sum"])
            vat = int(data["sum"]) * float(i.tax) / 100
            print(vat)
            total = int(data["sum"]) + vat
            li.append(total)
        list_of_total = li
        print(li)
        context = {"list":li}
        '''
        # only show 4 invoices at a time
        context = order_invoice[:6]
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


def invoice(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            print(request.POST)
            user = request.user
            #role = request.POST["title"]
            print(request.POST)
            # brand_name = request.POST["brand_name"]
            tax = request.POST["tax"]
            item = request.POST["item"]
            price = request.POST["price"]
            quantity = request.POST["quantity"]
            #total = request.POST["total"] or None
            to_full_name = request.POST["to_name"]
            #bank_name = request.POST["bank_name"]
            to_address = request.POST["to_address"]
            #account_name = request.POST["account_name"]
            account_number = request.POST["account_number"]
            from_phone = request.POST["from_phone"]
            from_full_name = request.POST["from_full_name"]
            from_address = request.POST["from_address"]
            to_phone = request.POST["to_phone"]
            to_email = request.POST["to_email"]
            from_email = request.POST["from_email"]
            print(request.POST)
            #tran = Transaction.objects.create(price=price, item=item, quantity=quantity, total=1)
            if tax == '':
                tax = 0
            xo = Invoice.objects.create(user=user, to_phone=to_phone,from_web_address=from_address,
                    to_address=to_address, account_number=account_number,
                    from_full_name=from_full_name, from_phone=from_phone,
                    to_full_name=to_full_name, from_email=from_email,
                    to_email=to_email,tax=tax )

            xo.transactions.create(price=price, item=item, quantity=quantity, total=1)
            data = xo.transactions.aggregate(sum = Sum(F('quantity') * F('price')))
            vat = int(data["sum"]) * float(xo.tax) / 100
            total = int(data["sum"]) + vat
            context = {"obj":xo, "sum":data["sum"],"vat":vat, "total":total}
            return render(request, "preview_template_1.html", context)
        return redirect('login')
    else:
        if request.user.is_authenticated:
            try:
                count = Invoice.objects.filter(user=request.user).last().id + 1
                return render(request, "invoice-gen.html", {"count":count})
            except AttributeError:
                return render(request, "invoice-gen.html")
        return render(request, "invoice-gen.html")



