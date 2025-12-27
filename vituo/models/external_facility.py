from django.db import models
from .college import College


class ExternalIslamicFacility(models.Model):
    facility_id = models.AutoField(primary_key=True)
    college = models.ForeignKey(
        College,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Chuo Kinachohusika"
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Jina la Kituo/Eneo"
    )
    location = models.CharField(
        max_length=500,
        verbose_name="Mahali/Anwani"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.college:
            return f"{self.name} - {self.college.name}"
        return f"{self.name} (Independent)"

    class Meta:
        verbose_name = "Kituo cha Kiislamu Nje ya Chuo"
        verbose_name_plural = "Vituo vya Kiislamu Nje ya Vyuo"
        ordering = ['name']