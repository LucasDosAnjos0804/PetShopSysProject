from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('',views.index, name = 'index'),
    path('menu_cliente/',views.menu_cliente,name='menu_cliente'),
    path('menu_gerente/',views.menu_gerente,name='menu_gerente'),
    path('menu_caixa/',views.menu_caixa,name='menu_caixa'),
    path('menu_veterinario/',views.menu_veterinario,name='menu_veterinario'),
]