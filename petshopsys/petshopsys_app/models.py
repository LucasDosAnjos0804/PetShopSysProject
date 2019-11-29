from django.db import models
from django.utils import timezone

# Create your models here.

# Implentar os status

class Usuario (models.Model):
    class Meta:
        abstract = True

    STATUS_USUARIO = (
        ('ONL','On-Line'),
        ('OFF','Off-Line'),
    )

    cpf = models.CharField (verbose_name = 'CPF', max_length = 11, primary_key = True)
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

    CARGO_CHOICES = (
        ("C","Caixa"),
        ("G","Gerente"),
        ("V","Veterinário"),
    )

    nome = models.CharField (verbose_name = 'Nome', max_length = 50)
    cargo = models.CharField (verbose_name = 'Cargo', max_length = 1, choices = CARGO_CHOICES)
    endereco = models.CharField (verbose_name = 'Endereço', max_length = 150)
    telefone = models.CharField (verbose_name = 'Telefonde',max_length = 14) # +pp(ee)nnnnn-nnnn
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

    STATUS_PET = (
        ('PC','Pet Cadastrado'),
        ('SA','Sendo Atendido'),
        ('VC','Vacinado'),
        ('IN','Internado'),
        ('FL','Falecido'),
    )

    #cod_pet é criado altomaticamente  pelo django
    cpf_dono = models.ForeignKey (Cliente, on_delete = models.CASCADE)
    nome = models.CharField (verbose_name = 'Nome',max_length = 150)
    tipo = models.CharField (verbose_name = 'Tipo', max_length = 50)

    status_pet = models.CharField (verbose_name = 'Status Pet', max_length = 2, choices = STATUS_PET)

    def __str__ (self):
        return self.nome

class RegistrarConsulta (models.Model):
    cod_pet = models.ForeignKey (Pet, on_delete = models.CASCADE)
    cod_veterinario = models.ForeignKey (Veterinario, on_delete = models.CASCADE)
    relatorio = models.TextField (verbose_name = 'Relatório')

    def __str__ (self):
        return self.cod_veterinario + " " + self.cod_veterinario 

class Servico (models.Model):

    STATUS_SERVICO = (
        ('AG','Agendado'),
        ('CO','Concluído'),
        ('CA','Cancelado'),
    )

    #cod_servico é criado altomaticamente pelo Django
    nome = models.CharField (verbose_name = 'Nome', max_length = 150, unique = True)
    preco = models.FloatField (verbose_name = 'Preco')

    status_servico = models.CharField (verbose_name = 'Status Servico', max_length = 2, choices = STATUS_SERVICO)

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

    status_produto = models.CharField (verbose_name = 'Status Produto', max_length = 3, choices = STATUS_PRODUTO)   

    def __str__ (self):
        return self.nome
        
class Estoque (models.Model):
    cod_produto = models.ForeignKey (Produto, on_delete = models.CASCADE)
    quantidade = models.BigIntegerField (verbose_name = 'Quantidade')

    def __str__ (self):
        return self.cod_produto + " " + self.quantidade

class ItensCompra (models.Model):
    cod_produto = models.ForeignKey (Produto, on_delete = models.CASCADE)
    quantidade = models.IntegerField (verbose_name = 'Quantidade')
    preco = models.FloatField (verbose_name = 'Preço')

    def __str__ (self):
        return self.cod_produto + " " + self.quantidade + " " + self.preco

class ItensServico (models.Model):
    cod_servico = models.ForeignKey (Servico, on_delete = models.CASCADE)
    preco = models.FloatField (verbose_name = 'Preço')

    def __str__ (self):
        return self.cod_servico + " " + self.preco

class Compra (models.Model):
    cod_cliente = models.ForeignKey (Cliente, on_delete = models.CASCADE)
    cod_caixa = models.ForeignKey (Caixa, on_delete = models.CASCADE)

    data = models.DateTimeField (auto_now = True)

    cod_itens_servico = models.ManyToManyField (ItensServico)
    cod_itens_compra = models.ManyToManyField (ItensCompra)

    preco_total = models.FloatField (verbose_name = 'Preço total')


class NotaFiscal (models.Model):
    cod_compra = models.ForeignKey (Compra, on_delete = models.CASCADE)

    nome_cliente = models.CharField (verbose_name = 'Nome do Cliente', max_length = 150)
    nome_do_caixa = models.CharField (verbose_name = 'Nome do Caixa', max_length = 150)

    data_da_compra = models.DateTimeField (verbose_name = 'Data da Compra')

    nome_itens_produtos = models.TextField (verbose_name = 'Lista de Produtos')
    nome_itens_servicos = models.TextField (verbose_name = 'Lista de Serviços')

    preco_total = models.FloatField (verbose_name = 'Preco Total')