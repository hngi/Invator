from django.shortcuts import render
#import weasyprint
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from .models import Invoice, Transaction
from django.db.models import Sum, F
from datetime import datetime
from django.conf import settings


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
    html_string = render_to_string('invoice/02.html', context)
    html = HTML(string=html_string,
    base_url=request.build_absolute_uri())
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
        # only show 4 invoices at a time
        context = order_invoice[:4]
        return render(request, "dashboard.html", {'data': context})
    return render(request, "dashboard.html")

def invoice(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            #role = request.POST["title"]
            item = request.POST["item"]
            #invoice_nam = request.POST["name"] or None
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

            #tran = Transaction.objects.create(price=price, item=item, quantity=quantity, total=1)
            #tran.save()

            xo = Invoice.objects.create(user=user, to_phone=to_phone,
                    to_address=to_address, account_number=account_number,
                    from_full_name=from_full_name, from_phone=from_phone,
                    to_full_name=to_full_name)
            xo.save()

            # Can't save transactions. Dom't know why
            xo.transactions.create(price=price, item=item, quantity=quantity, total=1)
            xo.save()

            return render(request, "dashboard.html")


    return render(request, "invoice-gen.html")

