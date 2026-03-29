from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class R2Storage(S3Boto3Storage):
    bucket_name = 'your-r2-bucket'
    location = 'photos'

class SupabaseStorage(S3Boto3Storage):
    bucket_name = 'album'
    location = 'images'

class Image(models.Model):
    """
    Image URLs and WebP Thumbnail Data stored in Supabase Postgres.
    Add via /admin/ after running migrate.
    """
    img_r2 = models.FileField(storage=R2Storage(), upload_to='photos/', null=True, blank=True)
    img_s3 = models.FileField(storage=SupabaseStorage(), upload_to='thumbs/', null=True, blank=True)
    tags = models.JSONField(default=list, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)    

    def __str__(self):
        if self.date:
            return f"Photo #{self.id} ({self.date.strftime('%Y-%m-%d')})"
        return f"Photo #{self.id} (undated)"

    class Meta:
        ordering = ['-date']
