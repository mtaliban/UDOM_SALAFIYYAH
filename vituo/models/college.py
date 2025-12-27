from django.db import models


class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Jina la Chuo"
    )
    is_salafi = models.BooleanField(
        default=False,
        verbose_name="Je, ni Chuo cha Kisalafi?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Chuo"
        verbose_name_plural = "Vyuo"
        ordering = ['name']

