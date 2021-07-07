from django.urls import path

from .views import index, contato, produto, consulta

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('consulta/', consulta, name='consulta'),
]
