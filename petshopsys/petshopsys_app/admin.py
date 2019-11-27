from django.contrib import admin

# Register your models here.
from .models import Cliente,Gerente,Caixa,Veterinario,Pet,RegistrarConsulta,Servico,Fonecedor,Produto,Estoque,ItensCompra,ItensServico,Compra,NotaFiscal



admin.site.register(Cliente)
admin.site.register(Gerente)
admin.site.register(Caixa)
admin.site.register(Veterinario)
admin.site.register(Pet)
admin.site.register(RegistrarConsulta)
admin.site.register(Servico)
admin.site.register(Fonecedor)
admin.site.register(Produto)
admin.site.register(Estoque)
admin.site.register(ItensCompra)
admin.site.register(ItensServico)
admin.site.register(Compra)
admin.site.register(NotaFiscal)
