from django.db import models
from django.contrib.auth.models import User

class NewVehicleRegistration(models.Model):
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    plate_no = models.CharField(max_length=255)
    chassis_no = models.CharField(max_length=255)
    
    def __str__(self):
        return self.plate_no

class DocumentsRegistration(models.Model):
    
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/')
    def __str__(self):
        return self.name


class UploadingOfDocumentsPerVehicle(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(NewVehicleRegistration, on_delete=models.CASCADE)
    document = models.ForeignKey(DocumentsRegistration, on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vehicle} - {self.document.name}"


class Invoices(models.Model):
    vehicle = models.ForeignKey(NewVehicleRegistration, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vehicle} - {self.invoice_no}"

class Proforma(models.Model):
    vehicle = models.ForeignKey(NewVehicleRegistration, on_delete=models.CASCADE)
    proforma_no = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vehicle} - {self.proforma_no}"



class ExpensePerVehicle(models.Model):
    vehicle = models.ForeignKey(NewVehicleRegistration, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=255)
    expense_date = models.DateField()
    expense_amount = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.vehicle} - {self.expense_name}"