from django.db import models

# Create your models here.
class PhnSlider(models.Model):
    phn_phone = models.CharField(max_length=200, verbose_name='Телефон')
    def __str__(self):
        return self.phn_phone

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

