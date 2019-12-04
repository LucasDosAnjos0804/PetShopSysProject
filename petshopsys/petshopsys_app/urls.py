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


    path('CadFuncionario/',views.cadFuncionario,name='CadFuncionario'),

    path('CadFuncionario/gerente/cadGerente/',views.cadGerente,name='CadGerente'),
    path('CadFuncionario/gerente/listGerente/',views.listGerente,name='ListGerente'),
    path('CadFuncionario/gerente/editGerente/<int:pk>',views.editGerente,name='EditGerente'),
    path('CadFuncionario/gerente/delGerente/<int:pk>',views.delGerente,name='DelGerente'),


    path('CadFuncionario/gerente/cadVeterinario/',views.cadVeterinario,name='CadVeterinario'),
    path('CadFuncionario/gerente/listVeterinario/',views.listVeterinario,name='ListVeterinario'),
    path('CadFuncionario/gerente/editVeterinario/<int:pk>',views.editVeterinario,name='EditVeterinario'),
    path('CadFuncionario/gerente/delVeterinario/<int:pk>',views.delVeterinario,name='DelVeterinario'),


    path('CadFuncionario/gerente/cadCaixa/',views.cadCaixa,name='CadCaixa'),
    path('CadFuncionario/gerente/listCaixa/',views.listCaixa,name='ListCaixa'),
    path('CadFuncionario/gerente/editCaixa/<int:pk>',views.editCaixa,name='EditCaixa'),
    path('CadFuncionario/gerente/delCaixa/<int:pk>',views.delCaixa,name='DelCaixa'),


    path('gerente/cadEstoque/',views.cadEstoque,name='CadEstoque'),
    path('gerente/listEstoque/',views.listEstoque,name='ListEstoque'),
    path('gerente/editEstoque/<int:pk>',views.editEstoque,name='EditEstoque'),
    path('gerente/delEstoque/<int:pk>',views.delEstoque,name='DelEstoque'),
########################################################

]