from django.db import models
from user.models import User
from user.utils.models import AbstractModel, AbstractManager


class Wallet(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Carteira de {self.user.username}"


class Transfer(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfer_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfer_received')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transferência de {self.from_user.username} para {self.to_user.username}"
