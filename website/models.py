from django.db import models


# django adds an s after the class name, so it appears as Records in admin layer
class Record(models.Model):
    # need to make migrations for django to convert this into database code
    # then migrate that code
    # to add the timestamp when it was created
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    # display_id = models.CharField(max_length=10)


    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
