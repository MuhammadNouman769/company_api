from django.db import models
from apps.company_api.choices import Choices, Organisation

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

   
    organisation = models.CharField(
        max_length=100,
        choices=Organisation
    )

    location = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=Choices)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    ceo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Company"
