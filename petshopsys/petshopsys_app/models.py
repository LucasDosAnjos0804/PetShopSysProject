from django.db import models
from django.utils import timezone

# Create your models here.


class Usuario (models.Model):
    class Meta:
        abstract = True

    STATUS_USUARIO = (
        ('ONL','On-Line'),
        ('OFF','Off-Line'),
    )

    cpf = models.CharField (verbose_name = 'CPF', max_length = 11, primary_key = True,unique=True)
    senha = models.CharField (verbose_name = 'Senha', max_length = 50, default = '00000')

    status_usuario = models.CharField (verbose_name = 'Status Usuario', max_length = 3, choices = STATUS_USUARIO, default = STATUS_USUARIO[1])

    # def login(self):
        

    def __str__(self):
        return self.cpf


class Cliente (Usuario):
    #cpf,senha veem de usuario  
    nome = models.CharField (verbose_name = 'Nome', max_length = 50)
    telefone = models.CharField (verbose_name = 'Telefone', max_length = 14) # +pp(ee)nnnnn-nnnn
    endereco = models.CharField (verbose_name = 'Endereço', max_length = 150)
    
    def __str__ (self):
        return self.nome

class Funcionario (Usuario):
    class Meta:
        abstract = True

    STATUS_FUNCIONARIO = (
        ('E','Empregado'),
        ('DC','Demitido Com Justa Causa'),
        ('DS','Demitido Sem Justa Causa'),
    )

    nome = models.CharField (verbose_name = 'Nome', max_length = 50)
    
    endereco = models.CharField (verbose_name = 'Endereço', max_length = 150)
    telefone = models.CharField (verbose_name = 'Telefone',max_length = 14) # +pp(ee)nnnnn-nnnn
    # e o gerente?
    status_funcionario = models.CharField (verbose_name = 'Status Funcionario', max_length = 2, choices = STATUS_FUNCIONARIO)

    def __str__ (self):
        return self.nome


class Gerente (Funcionario):
    #implementar metodos
    
    def __str__ (self):
        return self.nome

class Caixa (Funcionario):
    #Implementar metodos
    gerente = models.ForeignKey (Gerente, on_delete = models.CASCADE)

    def __str__ (self):
        return self.nome

class Veterinario (Funcionario):
    #implementar metodos
    gerente = models.ForeignKey (Gerente,  on_delete = models.CASCADE)

    def __str__ (self):
        return self.nome

class Pet (models.Model):
    
    #cod_pet é criado altomaticamente  pelo django
    cpf_dono = models.ForeignKey (Cliente, on_delete = models.CASCADE)
    nome = models.CharField (verbose_name = 'Nome',max_length = 150)
    tipo = models.CharField (verbose_name = 'Tipo', max_length = 50)

    def __str__ (self):
        return self.nome

class RegistrarConsulta (models.Model):
    cod_pet = models.ForeignKey (Pet, on_delete = models.CASCADE)
    cod_veterinario = models.ForeignKey (Veterinario, on_delete = models.CASCADE)

    data_consulta = models.DateTimeField(verbose_name='Data da Consulta')
    
    relatorio = models.TextField (verbose_name = 'Relatório')

    data_retorno = models.DateField (verbose_name='Data de Retorno')

    def __str__ (self):
        return self.relatorio

class Servico (models.Model):

    #cod_servico é criado altomaticamente pelo Django
    nome = models.CharField (verbose_name = 'Nome', max_length = 150, unique = True)
    preco = models.FloatField (verbose_name = 'Preco')

    def __str__ (self):
        return self.nome

class Fornecedor (models.Model):
    cnpj = models.CharField (verbose_name = 'CNPJ', max_length = 14, unique = True)
    nome = models.CharField (verbose_name = 'Nome', max_length = 50)
    endereco = models.CharField (verbose_name = 'Endereco', max_length = 150) 
    telefone = models.CharField (verbose_name = 'Telefone', max_length = 14) # +pp(ee)nnnnn-nnnn

    def __str__ (self):
        return self.nome

class Produto (models.Model):

    STATUS_PRODUTO = (
        ('EST','Estocado'),
        ('EXP','Expirado'),
        ('VEN','Vendido'),
    )

    # cod_produto é criado altomaticamente pelo Django
    cod_fornecedor = models.ForeignKey (Fornecedor, on_delete = models.CASCADE)
    nome = models.CharField (verbose_name = 'Nome', max_length = 150, unique = True)
    data_de_validade = models.DateField (verbose_name = 'Data de validade')
    preco = models.FloatField (verbose_name = 'Preço')

    status_produto = models.CharField (verbose_name = 'Status Produto', max_length = 3, choices = STATUS_PRODUTO,default=STATUS_PRODUTO[1])

    def __str__ (self):
        return self.nome
        
class Estoque (models.Model):
    cod_produto = models.ForeignKey (Produto, on_delete = models.CASCADE)
    quantidade = models.BigIntegerField (verbose_name = 'Quantidade')

    def __str__ (self):
        return str(self.pk)

class ItemCompra (models.Model):
    cod_produto = models.OneToOneField (Produto,on_delete=models.CASCADE)
    quantidade = models.IntegerField (verbose_name = 'Quantidade')
    preco = models.FloatField (verbose_name = 'Preço')

    def __str__ (self):
        return Produto.objects.filter(itemcompra__cod_produto = self.cod_produto).get().nome

class ItemServico (models.Model):
    cod_servico = models.OneToOneField (Servico,on_delete=models.CASCADE)
    cod_registrar_sevico = models.ForeignKey (RegistrarConsulta, on_delete=models.CASCADE)
    quantidade = models.IntegerField (verbose_name = 'Quantidade')
    preco = models.FloatField (verbose_name = 'Preço')

    def __str__ (self):
        return Servico.objects.filter (itemservico__cod_servico = self.cod_servico).get().nome

class ListaItemServico (models.Model):
    cod_item_servico = models.ManyToManyField (ItemServico)

    def __str__ (self):
        return str(self.cod_item_servico)

class ListaItemCompra (models.Model):
    cod_item_compra = models.ManyToManyField (ItemCompra)
    def __str__ (self):
        return str(self.cod_item_compra)

class Compra (models.Model):
    cod_cliente = models.ForeignKey (Cliente, on_delete = models.CASCADE)
    cod_caixa = models.ForeignKey (Caixa, on_delete = models.CASCADE)
    
    data = models.DateTimeField (auto_now = True)

    cod_lista_item_compra = models.OneToOneField (ListaItemCompra,null=True, on_delete=models.CASCADE)
    cod_lista_item_servico = models.OneToOneField (ListaItemServico,null=True,on_delete=models.CASCADE)

    preco_total = models.FloatField (verbose_name = 'Preço total')

    def __str__ (self):
        return str(self.pk)


class NotaFiscal (models.Model):
    cod_compra = models.ForeignKey (Compra, on_delete = models.CASCADE)

    nome_cliente = models.CharField (verbose_name = 'Nome do Cliente', max_length = 150)
    nome_do_caixa = models.CharField (verbose_name = 'Nome do Caixa', max_length = 150)

    data_da_compra = models.DateTimeField (verbose_name = 'Data da Compra')

    lista_item_produtos = models.TextField (verbose_name = 'Lista de Produtos')
    lista_item_servicos = models.TextField (verbose_name = 'Lista de Serviços')

    preco_total = models.FloatField (verbose_name = 'Preco Total')

    def __str__ (self):
        return str(self.pk)