from django.db import models


class Quote(models.Model):
    text_en = models.TextField()
    text_ar = models.TextField()
    author_en = models.CharField(max_length=255)
    author_ar = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text_en} - {self.author_en}"