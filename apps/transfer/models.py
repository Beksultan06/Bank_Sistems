from django.db import models

# Create your models here.
from apps.users.models import Username

class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        Username,
        on_delete=models.CASCADE,
        related_name="from_user",
        verbose_name="От пользователя"
    )
    to_user = models.ForeignKey(
        Username,
        on_delete=models.CASCADE,
        related_name="to_user",
        verbose_name="Пользователю"
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    amount = models.CharField(
        max_length=255,
        verbose_name="Количество"
    )
    def __str__(self):
        return self.from_user
    
    class Meta:
        verbose_name = "История"
        verbose_name_plural = "История"
