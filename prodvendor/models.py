from django.db import models
# Create your models here.


class Prodvendor(models.Model):
    vendorname = models.CharField(max_length=150, unique=True)
    vendorcodename = models.CharField(max_length=150, blank=True, null=True)
    vendorcategory = models.CharField(max_length=150, blank=True, null=True)
    numvendorproducts = models.CharField(
        max_length=150, default='0', blank=True, null=True)
    vendornote = models.CharField(max_length=150, blank=True, null=True)
    vendorweburl = models.CharField(max_length=150, blank=True, null=True)
    contact1name = models.CharField(max_length=150, blank=True, null=True)
    contact1phone = models.CharField(max_length=150, blank=True, null=True)
    contact1email = models.CharField(max_length=150, blank=True, null=True)
    contact2name = models.CharField(max_length=150, blank=True, null=True)
    contact2phone = models.CharField(max_length=150, blank=True, null=True)
    contact2email = models.CharField(max_length=150, blank=True, null=True)
    contractnum = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.vendorname

    class Meta:
        ordering = ('vendorname',)
