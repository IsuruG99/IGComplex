from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class TrackerBannerStorage(S3Boto3Storage):
    bucket_name = 'hub'
    location = 'tracker' 

class Gacha(models.Model):
    """
    Game Data stored in Supabase Postgres.
    Game Covers inside Supabase Storage.
    Add via /admin/ after running migrate.
    """
    title = models.CharField(max_length=200, verbose_name="Game Title")
    year = models.IntegerField(verbose_name="Release Year")
    pity_num_std = models.IntegerField(verbose_name="Std Soft Pity", help_text="e.g. 40")
    pity_max_std = models.IntegerField(verbose_name="Std Hard Pity", help_text="e.g. 90")
    pity_num_lim = models.IntegerField(verbose_name="Limited Soft Pity", help_text="e.g. 40")
    pity_max_lim = models.IntegerField(verbose_name="Limited Hard Pity", help_text="e.g. 90")
    gr_lim = models.BooleanField(verbose_name="Limited Guaranteed?")
    pity_num_wep = models.IntegerField(verbose_name="Weapon Soft Pity", help_text="e.g. 30")
    pity_max_wep = models.IntegerField(verbose_name="Weapon Hard Pity", help_text="e.g. 90")
    gr_wep = models.BooleanField(verbose_name="Weapon Guaranteed?")
    banner = models.ImageField(storage=TrackerBannerStorage(), null=True, verbose_name="Banner Image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        ordering = ['title']
