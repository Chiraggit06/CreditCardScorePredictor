from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class predict_model(models.Model):
     gender=models.CharField(max_length=10)
     education=models.CharField(max_length=10)
     marital_status=models.CharField(max_length=10)
     age=models.CharField(max_length=10)
     limit=models.CharField(max_length=10)
     repay_april=models.CharField(max_length=10)
     repay_may=models.CharField(max_length=10)
     repay_june=models.CharField(max_length=10)
     repay_july=models.CharField(max_length=10)
     repay_aug=models.CharField(max_length=10)
     repay_sep=models.CharField(max_length=10)
     bill_april=models.CharField(max_length=10)
     bill_may=models.CharField(max_length=10)
     bill_june=models.CharField(max_length=10)
     bill_july=models.CharField(max_length=10)
     bill_aug=models.CharField(max_length=10)
     bill_sep=models.CharField(max_length=10)
     prev_april=models.CharField(max_length=10)
     prev_may=models.CharField(max_length=10)
     prev_june=models.CharField(max_length=10)
     prev_july=models.CharField(max_length=10)
     prev_aug=models.CharField(max_length=10)
     prev_sep=models.CharField(max_length=10)
     default_pay=models.CharField(max_length=10)