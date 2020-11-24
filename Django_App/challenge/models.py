from django.db import models

# Create your models here.


class User(models.Model):
    # null True - allows for field to be empty
    name = models.CharField(max_length=200, null=True)
    nickname = models.CharField(max_length=200, null=True)
    profile_image = models.CharField(max_length=200, null=True)
    # automatically determines when a user is added to the DB
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # Shows User Name in admin panel
    def _str_(self):
        return self.name
