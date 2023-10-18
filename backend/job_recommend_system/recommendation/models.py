from django.db import models

# Create your models here.
class JobRecommendation(models.Model):
    job_title = models.CharField(max_length=200)
    # Add any other fields relevant to the recommended jobs