from django.contrib import admin

# Register your models here.
from .models import Cliente,Gerente,Caixa,Veterinario,Pet,RegistrarConsulta,Servico,Fornecedor,Produto,Estoque,ItemCompra,ItemServico,Compra,NotaFiscal,ListaItemCompra,ListaItemServico



admin.site.register(Cliente)
admin.site.register(Gerente)
admin.site.register(Caixa)
admin.site.register(Veterinario)
admin.site.register(Pet)
admin.site.register(RegistrarConsulta)
admin.site.register(Servico)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Estoque)
admin.site.register(ItemCompra)
admin.site.register(ItemServico)
admin.site.register(Compra)
admin.site.register(NotaFiscal)
admin.site.register(ListaItemServico)
admin.site.register(ListaItemCompra)


#nota de rodape

