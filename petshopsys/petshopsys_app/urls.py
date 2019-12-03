from django.urls import path
from .views import Login,Index,MenuCliente,MenuGerente,MenuCaixa,MenuVeterinario,cadFornecedor,cadServico,listServico,detServico,editServico

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
    path('detailFornecedor/<int:pk>',views.detFornecedor,name='DetFornecedor'),
    path('editFornecedor/<int:pk>',views.editFornecedor,name='EditFornecedor'),

    path('cadServico/',views.cadServico,name='CadServico'),
    path('listServico/',views.listServico,name='ListServico'),
    path('detailServico/<int:pk>',views.detServico,name='DetServico'),
    path('editServico/<int:pk>',views.editServico,name='EditServico'),
]