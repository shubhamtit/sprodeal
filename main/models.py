from django.db import models

class UserSubmission(models.Model):
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    pin = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} — {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "User Submission"
        verbose_name_plural = "User Submissions"