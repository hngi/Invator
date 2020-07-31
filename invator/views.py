from django.shortcuts import render
import weasyprint
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.http import Http404, HttpResponse
from .models import Invoice
from django.db.models import Sum, F
from datetime import datetime


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