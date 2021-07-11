from django.urls import path

from .views import index, contato, produto, consulta1

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('consulta/<int:pk>', consulta1, name='consulta1'),
    
]
