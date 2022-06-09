from django.db import models
from utils.date_script import format_date_actual_for_file as date_file

# Create your models here.
class StatisticDataUpload(models.Model):
    database_file = models.FileField("Arquivo com os dados estatísticos:", upload_to=f'files/database/{ date_file() }')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
