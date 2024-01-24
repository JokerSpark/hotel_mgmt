from django.db import models

# Create your models here.
position = {
        "Housekeeping": "Housekeeping",
        "Security": "Security",
        "Supervisor": "Supervisor",
        "Manager": "Manager",
        "Human Resources": "Human Resources",
    }

class Staff(models.Model):
    Staff_name = models.CharField(max_length=30)
    Staff_address = models.CharField(max_length=30)
    Staff_no = models.CharField(max_length=30)
    Staff_position = models.CharField(max_length=20, choices=position)

    def __str__(self):
        return f'{self.Staff_name} - {self.Staff_position}'

room_ty = {
        "Deluxe Room": "Deluxe Room",
        "Single room": "Single room",
        "King room":"King room"
        
    }

class Room(models.Model):
    room_no = models.CharField(max_length=30)
    room_type = models.CharField(max_length=20, choices=room_ty)

    def __str__(self):
        return f'{self.room_no} - {self.room_type}'
    

res_ty = {
        "Fast food": "Fast food",
        "Cafeteria": "Cafeteria",
        "Bakery":"Bakery",
        "Family Style":"Family Style"
        
    }

class Restaurants(models.Model):
    res_name = models.CharField(max_length=30)
    res_type = models.CharField(max_length=20, choices=res_ty)
    res_user = models.CharField(max_length=30)
    res_pass = models.CharField(max_length=30)
    res_cpass = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.res_name} - {self.res_type}'
    

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    food_description = models.CharField(max_length=30)
    food_price = models.IntegerField()
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.food_name} - {self.food_name} - {self.food_price} rs'
    


class Customer(models.Model):
    cus_name = models.CharField(max_length=30)
    cus_username = models.CharField(max_length=30)
    cus_address = models.CharField(max_length=30)
    cus_id =models.FileField(upload_to ='uploads/',max_length=20000)
    cus_pass = models.CharField(max_length=30)
    cus_cpass = models.CharField(max_length=30)


    def __str__(self):
        return f'{self.cus_name}'