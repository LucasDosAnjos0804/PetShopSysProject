from django.urls import path
from .views import Login,Index,MenuCliente,MenuGerente,MenuCaixa,MenuVeterinario,cadFornecedor,cadServico,listServico,editServico

from . import views
urlpatterns = [
    path('',Index.as_view(), name = 'Index'),

    path('login/<str:user>', Login.as_view(), name = 'Login'),
    
    path('cliente/<str:cli>', MenuCliente.as_view() , name='MenuCliente'),
    path('gerente/',MenuGerente.as_view(),name='MenuGerente'),
    path('caixa/',MenuCaixa.as_view(),name='MenuCaixa'),
    path('veterinario/',MenuVeterinario.as_view(),name='MenuVeterinario'),

    path('cadFornecedor/',views.cadFornecedor,name='CadFornecedor'),
    path('listFornecedor/',views.listFornecedor,name='ListFornecedor'),
    path('editFornecedor/<int:pk>',views.editFornecedor,name='EditFornecedor'),

    path('cadServico/',views.cadServico,name='CadServico'),
    path('listServico/',views.listServico,name='ListServico'),
    path('editServico/<int:pk>',views.editServico,name='EditServico'),

    path('cadCliente/',views.cadCliente,name='CadCliente'),
    path('listCliente/',views.listCliente,name='ListCliente'),
    path('editCliente/<int:pk>',views.editCliente,name='EditCliente'),

    path('cadPet/',views.cadPet,name='CadPet'),
    path('listPet/',views.listPet,name='ListPet'),
    path('editPet/<int:pk>',views.editPet,name='EditPet'),

    path('cadProduto/',views.cadProduto,name='CadProduto'),
    path('listProduto/',views.listProduto,name='ListProduto'),
    path('editProduto/<int:pk>',views.editProduto,name='EditProduto'),
]