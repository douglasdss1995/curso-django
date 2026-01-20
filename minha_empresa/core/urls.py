from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register('funcionario', viewsets.FuncionarioViewSet)
router.register('departamento', viewsets.DepartamentoViewSet)
router.register('vendedor', viewsets.VendedorViewSet)
router.register('produto', viewsets.ProdutoViewSet)
router.register('venda', viewsets.VendaViewSet)
router.register('venda_item', viewsets.VendaItemViewSet)

urlpatterns = router.urls
