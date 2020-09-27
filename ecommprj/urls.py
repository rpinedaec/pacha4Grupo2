"""ecommprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from ecommapp import views
from rest_framework import permissions

from rest_framework_simplejwt import views as jwt_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

#from rest_framework.authtoken import views as views1

schema_view = get_schema_view(   
    openapi.Info(      
        title="PachaQtec Hackaton Final Grupo 2",     
        default_version='v1',      
        description="Descripcion de APIS",      
        terms_of_service="https://www.google.com/policies/terms/",      
        contact=openapi.Contact(email="contact@snippets.local"),      
        license=openapi.License(name="BSD License"),   
    ),   
    public=True,   
    permission_classes=(permissions.AllowAny,),
    )

router = routers.DefaultRouter()
router.register(r'cupones', views.CuponViewSet)
router.register(r'estado_pedido', views.Estado_PedidoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'pedido', views.PedidoViewSet)
router.register(r'detalle_pedido', views.Detalle_pedidoViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),    
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),    
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #url(r'^api-token-auth/', views1.obtain_auth_token),
]