from django.db import models
from mongoengine import Document, fields
# Create your models here.


class Marketing(Document):
    Traffic = fields.StringField()
    Source = fields.StringField()
    Country = fields.StringField()
    Clicks = fields.IntField()
    CampaignCost = fields.IntField()
    CPC = fields.IntField()
    Users = fields.IntField()
    Sessions = fields.IntField()
    BounceRate = fields.StringField()
    Leads = fields.IntField()
    Opportunities = fields.IntField()
    Sates = fields.IntField()
    Date = fields.StringField()
    PurchaseCost = fields.StringField()


class transaction(Document):
    Country = fields.StringField()
    CustomerID = fields.IntField()
    Description = fields.StringField()
    InvoiceDate = fields.StringField()
    InvoiceNo = fields.IntField()
    Quantity = fields.IntField()
    StockCode = fields.StringField()
    UnitPrice = fields.IntField()

