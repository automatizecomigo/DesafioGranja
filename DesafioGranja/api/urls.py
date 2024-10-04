# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatoViewSet, ClienteViewSet, VendaViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'patos', PatoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vendas/', views.registrar_venda, name='registrar_venda'),
    path('vendas/listar/', views.listar_vendas, name='listar_vendas'),
    path('reports/excel/', views.gerar_relatorio_excel, name='gerar_relatorio_excel'),  # Novo endpoint para Excel
    path('reports/pdf/', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
]
