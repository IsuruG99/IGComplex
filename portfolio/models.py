from django.db import models

class Project(models.Model):
    """
    Projects stored in Supabase Postgres.
    Screenshots are manually uploaded to Supabase Storage (public bucket) and URL stored here.
    Add via /admin/ after running migrate.
    """
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    brief_desc = models.TextField()
    tech_stack = models.TextField(help_text="Comma-separated, e.g. Django, Supabase, Docker")
    screenshot_url = models.URLField(blank=True, null=True, help_text="Public URL from Supabase Storage S3 bucket")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        ordering = ['-year']
