from django import forms
from main import models

class staff_form(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = "__all__"


class room_form(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = "__all__"


class rest_form(forms.ModelForm):
    class Meta:
        model = models.Restaurants
        fields = "__all__"


class update_rest_form(forms.ModelForm):
    class Meta:
        model = models.Restaurants
        fields = ['res_name','res_type','res_user']



class Customer_form(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"


class update_customer_form(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['cus_name','cus_username','cus_address','cus_id']