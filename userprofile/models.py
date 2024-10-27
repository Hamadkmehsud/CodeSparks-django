from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.hashers import make_password, check_password


class UserRegisterModel(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Store the hashed password

    def set_password(self, raw_password):
        """Set the password using make_password for hashing."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Verify a password using check_password."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

class UserInfoModel(models.Model):
    user = models.OneToOneField(UserRegisterModel, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)  # Ensure email is unique
    image = models.ImageField(upload_to='profile_images/')  # Specify upload path
    phone = models.CharField(max_length=15)  # Use CharField for phone to accommodate formats
    about_user = models.TextField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
