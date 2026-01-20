from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, editable=False, null=False)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=False)
    is_ativo = models.BooleanField(default=True, null=False)

    class Meta:
        abstract = True


class Funcionario(BaseModel):
    nome = models.CharField(max_length=100)
    departamento = models.ForeignKey('Departamento', on_delete=models.RESTRICT, null=False)

    class Meta:
        managed = True


class Departamento(BaseModel):
    descricao = models.CharField(max_length=100)

    class Meta:
        managed = True


class Vendedor(BaseModel):
    nome = models.CharField(max_length=100)

    class Meta:
        managed = True


class Produto(BaseModel):
    descricao = models.CharField(max_length=100)

    class Meta:
        managed = True


class Venda(BaseModel):
    vendedor = models.ForeignKey('Vendedor', on_delete=models.RESTRICT, null=False)

    class Meta:
        managed = True


class VendaItem(BaseModel):
    venda = models.ForeignKey('Venda', on_delete=models.RESTRICT, null=False)
    produto = models.ForeignKey('Produto', on_delete=models.RESTRICT, null=False)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
