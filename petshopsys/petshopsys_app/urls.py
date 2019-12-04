from django.urls import path
from .views import Login,Index,MenuCliente,MenuGerente,MenuCaixa,MenuVeterinario,cadFornecedor,cadServico,listServico,editServico,cadFuncionario

from . import views

urlpatterns = [
    path('',Index.as_view(), name = 'Index'),

    path('login/<str:user>', Login.as_view(), name = 'Login'),
    
    path('cliente/<str:cli>', MenuCliente.as_view() , name='MenuCliente'),
    path('gerente/',MenuGerente.as_view(),name='MenuGerente'),
    path('caixa/',MenuCaixa.as_view(),name='MenuCaixa'),
    path('veterinario/',MenuVeterinario.as_view(),name='MenuVeterinario'),
#####################GERENTE#######################
    path('gerente/cadFornecedor/',views.cadFornecedor,name='CadFornecedor'),
    path('gerente/listFornecedor/',views.listFornecedor,name='ListFornecedor'),
    path('gerente/editFornecedor/<int:pk>',views.editFornecedor,name='EditFornecedor'),
    path('gerente/delFornecedor/<int:pk>',views.delFornecedor,name='DelFornecedor'),


    path('gerente/cadServico/',views.cadServico,name='CadServico'),
    path('gerente/listServico/',views.listServico,name='ListServico'),
    path('gerente/editServico/<int:pk>',views.editServico,name='EditServico'),
    path('gerente/delServico/<int:pk>',views.delServico,name='DelServico'),


    path('gerente/cadCliente/',views.cadCliente,name='CadCliente'),
    path('gerente/listCliente/',views.listCliente,name='ListCliente'),
    path('gerente/editCliente/<int:pk>',views.editCliente,name='EditCliente'),
    path('gerente/delCliente/<int:pk>',views.delCliente,name='DelCliente'),


    path('gerente/cadPet/',views.cadPet,name='CadPet'),
    path('gerente/listPet/',views.listPet,name='ListPet'),
    path('gerente/editPet/<int:pk>',views.editPet,name='EditPet'),
    path('gerente/delPet/<int:pk>',views.delPet,name='DelPet'),


    path('gerente/cadProduto/',views.cadProduto,name='CadProduto'),
    path('gerente/listProduto/',views.listProduto,name='ListProduto'),
    path('gerente/editProduto/<int:pk>',views.editProduto,name='EditProduto'),
    path('gerente/delProduto/<int:pk>',views.delProduto,name='DelProduto'),


    path('gerente/CadFuncionario/',views.cadFuncionario,name='CadFuncionario'),

    path('gerente/CadFuncionario/cadGerente/',views.cadGerente,name='CadGerente'),
    path('gerente/CadFuncionario/listGerente/',views.listGerente,name='ListGerente'),
    path('gerente/CadFuncionario/editGerente/<int:pk>',views.editGerente,name='EditGerente'),
    path('gerente/CadFuncionario/delGerente/<int:pk>',views.delGerente,name='DelGerente'),


    path('gerente/CadFuncionario/cadVeterinario/',views.cadVeterinario,name='CadVeterinario'),
    path('gerente/CadFuncionario/listVeterinario/',views.listVeterinario,name='ListVeterinario'),
    path('gerente/CadFuncionario/editVeterinario/<int:pk>',views.editVeterinario,name='EditVeterinario'),
    path('gerente/CadFuncionario/delVeterinario/<int:pk>',views.delVeterinario,name='DelVeterinario'),


    path('gerente/CadFuncionario/cadCaixa/',views.cadCaixa,name='CadCaixa'),
    path('gerente/CadFuncionario/listCaixa/',views.listCaixa,name='ListCaixa'),
    path('gerente/CadFuncionario/editCaixa/<int:pk>',views.editCaixa,name='EditCaixa'),
    path('gerente/CadFuncionario/delCaixa/<int:pk>',views.delCaixa,name='DelCaixa'),


    path('gerente/cadEstoque/',views.cadEstoque,name='CadEstoque'),
    path('gerente/listEstoque/',views.listEstoque,name='ListEstoque'),
    path('gerente/editEstoque/<int:pk>',views.editEstoque,name='EditEstoque'),
    path('gerente/delEstoque/<int:pk>',views.delEstoque,name='DelEstoque'),
########################################################


]