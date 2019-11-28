from django.urls import path
from .views import Login,Index

urlpatterns = [
    path('',Index.as_view(), name = 'Index'),
    path('login/<str:user>', Login.as_view(), name = 'Login'),
    # path('menu_cliente/',views.menu_cliente,name='menu_cliente'),
    # path('menu_gerente/',views.menu_gerente,name='menu_gerente'),
    # path('menu_caixa/',views.menu_caixa,name='menu_caixa'),
    # path('menu_veterinario/',views.menu_veterinario,name='menu_veterinario'),
]