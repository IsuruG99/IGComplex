from django.db import models
import os
from storages.backends.s3boto3 import S3Boto3Storage


class BlogStorage(S3Boto3Storage):
    bucket_name = 'blog'
    location = 'articles'
    endpoint_url = os.getenv('SUPABASE_STORAGE_URL')
    access_key = os.getenv('SUPABASE_ACCESS_KEY')
    secret_key = os.getenv('SUPABASE_SECRET_KEY')
    region_name = os.getenv('SUPABASE_REGION', 'ap-south-1')
    querystring_auth = True
    default_acl = 'public-read'
    signature_version = 's3v4'


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Article Title')
    description = models.TextField(blank=True)
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date', null=True, blank=True)
    image_1 = models.ImageField(storage=BlogStorage(), upload_to='', null=True, blank=True)
    image_2 = models.ImageField(storage=BlogStorage(), upload_to='', null=True, blank=True)
    image_3 = models.ImageField(storage=BlogStorage(), upload_to='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def images(self):
        return [image for image in (self.image_1, self.image_2, self.image_3) if image]

    class Meta:
        ordering = ['-start_date', '-created_at', '-id']
