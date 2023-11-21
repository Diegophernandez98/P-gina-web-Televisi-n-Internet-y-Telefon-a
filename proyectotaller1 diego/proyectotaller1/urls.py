from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('planes_telefonia', views.planes_telefonia, name="planes_telefonia"),
    path('planes_internet/', views.planes_internet, name='planes_internet'),
    path('planes_television/', views.planes_television, name='planes_television'),
    path('resumen_plan_internet/<int:plan_id>/', views.resumen_plan_internet, name='resumen_plan_internet'),
    path('resumen_plan_television/<int:plan_id>/', views.resumen_plan_television, name='resumen_plan_television'),
    path('resumen_plan_telefonia/<int:plan_id>/', views.resumen_plan_telefonia, name='resumen_plan_telefonia'),
    path('planS/', views.planS, name="planS"),
    path('planM/', views.planM, name="planM"),
    path('planL/', views.planM, name="planL"),
    path('planXL/', views.planM, name="planXL"),
    path('inicioSesion/', views.login_view, name="login"),
    path('cerrarSesion/', views.cerrarSesion, name="cerrarSesion"),
    path('confirmar_suscripcion/', views.confirmar_suscripcion, name='confirmar_suscripcion'),
    path('cliente_dashboard/', views.cliente_dashboard, name='cliente_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('empleado_dashboard/', views.empleado_dashboard, name='empleado_dashboard'),
    path('registro/', views.registro, name="registro"),
    path('editar_perfil/', views.editar_perfil, name="editar_perfil"),
    path('enviar_comentario/', views.enviar_comentario, name="enviar_comentario"),
    path('editar_plan_telefonia/', views.editar_plan_telefonia, name='editar_plan_telefonia'),
    path('editar_plan_television/', views.editar_plan_television, name='editar_plan_television'),
    path('editar_plan_internet/', views.editar_plan_internet, name='editar_plan_internet')
]