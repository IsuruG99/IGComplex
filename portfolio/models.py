from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class PortfolioScreenshotStorage(S3Boto3Storage):
    bucket_name = 'portfolio'
    location = 'screenshots' 

class PortfolioStorage(S3Boto3Storage):
    bucket_name = 'portfolio'
    location = 'others'

class Project(models.Model):
    """
    Projects stored in Supabase Postgres.
    Screenshots are manually uploaded to Supabase Storage (public bucket) and URL stored here.
    Add via /admin/ after running migrate.
    """
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    brief = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True)
    tech_stack = models.TextField(help_text="Comma-separated, e.g. Django, Supabase, Docker")
    screenshot_1 = models.ImageField(storage=PortfolioScreenshotStorage(), null=True)
    screenshot_2 = models.ImageField(storage=PortfolioScreenshotStorage(), null=True, blank=True)
    screenshot_3 = models.ImageField(storage=PortfolioScreenshotStorage(), null=True, blank=True)
    github = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        ordering = ['-year']
