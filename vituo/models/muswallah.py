from django.db import models
from .college import College


class Muswallah(models.Model):
    muswallah_id = models.AutoField(primary_key=True)
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        related_name='miswallah',
        verbose_name="Chuo"
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Jina la Msikiti/Muswallah"
    )
    is_salafi = models.BooleanField(
        default=False,
        verbose_name="Je, ni ya Kisalafi?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.college.name}"

    class Meta:
        verbose_name = "Muswallah/Msikiti"
        verbose_name_plural = "Miswallah/Misikiti"
        ordering = ['name']