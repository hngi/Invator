from django.db import models
import uuid
from django.contrib.auth import get_user_model
from .constants import STATUS

User = get_user_model()

# Create your models here.
"""
Name of client
Type of work done
Amount to be payed
Hours spent (optional)
Amount by hour(if it was an hourly job)
Amount by contract
"""
# class Invator(models.Model):
#     Name = models.CharField(max_length=255,verbose_name='name')
#     Workdone = models.CharField(max_length=255)
#     Amount = models.CharField(max_length=2550000)
#     HourAmount = models.CharField(max_length=2550000)
#     ContractAmount = models.CharField(max_length=2550000)


class Transaction(models.Model):
    item = models.CharField(max_length=150 ,null=True, blank=True)
    price = models.CharField(max_length=30, null=True, blank=True)
    quantity = models.CharField(max_length=30, null=True, blank=True)
    total = models.CharField(max_length=30, null=True, blank=True)
    #status = models.CharField(max_length=9, choices=STATUS, default='')


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #invoice_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title  = models.CharField(max_length=255, null=True, blank=True)
    to_full_name = models.CharField(max_length=255, null=True, blank=True)
    to_address = models.CharField(max_length=500, null=True, blank=True)
    to_email = models.EmailField(max_length=255, null=True, blank=True)
    to_phone = models.CharField(max_length=15, null=True, blank=True)
    from_full_name = models.CharField(max_length=255, null=True, blank=True)
    from_phone = models.CharField(max_length=15, null=True, blank=True)
    # role -is the user an entrepreneur, a sales-person, assistant manager
    role = models.CharField(max_length=150, null=True, blank=True)
    account_name = models.CharField(max_length=150, null=True, blank=True)
    account_number = models.CharField(max_length=150, null=True, blank=True)
    # bank name and address
    bank_name = models.CharField(max_length=150, null=True, blank=True)
    from_web_address = models.CharField(max_length=150, null=True, blank=True)
    tax = models.CharField(max_length=15, null=True, blank=True)
    brand_name = models.CharField(max_length=150, null=True, blank=True)
    terms = models.CharField(max_length=300, null=True, blank=True)
    from_email = models.EmailField(max_length=255, null=True, blank=True)
    transactions = models.ManyToManyField(Transaction)
    date_created = models.DateField(auto_now_add=True)
    grand_total = models.IntegerField(null=True, blank=True)
    # just for tracking recents
    time = models.DateTimeField(auto_now_add=True)

