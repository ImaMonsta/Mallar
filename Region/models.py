from django.db import models
from django.contrib.auth.models import User

REGION_TYPES = (
    ('E', 'Estado'),
    ('M', 'Municipio'),
    ('DL', 'Distrito Local'),
    ('DF', 'Distrito Federal'),
    ('S', 'Seccion')
)


# Create your models here.
class Region(models.Model):
    id_description = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    region_type = models.CharField(max_length=2, default='E', choices=REGION_TYPES)

    def __str__(self):
        return "{0} - {1}".format(self.id_description, self.description)

class Region_Estructura(models.Model):
    father_region = models.ForeignKey(Region, related_name="region_father")
    son_region = models.ForeignKey(Region, related_name="region_son")
