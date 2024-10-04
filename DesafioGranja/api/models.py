# models.py
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    elegivel_desconto = models.BooleanField(default=False)

class Pato(models.Model):
    nome = models.CharField(max_length=100)
    mae = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    filhos = models.IntegerField(default=0)

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    patos = models.ManyToManyField(Pato)
    data_venda = models.DateTimeField(auto_now_add=True)

    def valor_total(self):
        # Aqui você deve implementar a lógica para calcular o valor total da venda
        total = 0
        for pato in self.patos.all():
            if pato.filhos == 1:
                total += 50.00
            elif pato.filhos == 2:
                total += 25.00
            else:
                total += 70.00

        # Aplicar desconto se o cliente for elegível
        if self.cliente.elegivel_desconto:
            total *= 0.8  # 20% de desconto

        return total
