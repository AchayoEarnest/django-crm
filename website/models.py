from django.db import models

class Record(models.Model):  # Changed class name to singular
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)  # Use EmailField for validation
    phone = models.CharField(max_length=15)  # Reduced max_length for a phone number
    address = models.CharField(max_length=255)  # Increased max_length for flexibility
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
