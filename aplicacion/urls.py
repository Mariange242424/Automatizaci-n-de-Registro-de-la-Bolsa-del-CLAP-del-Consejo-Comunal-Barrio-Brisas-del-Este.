from django.urls import path
from . import views
from .views import  CalleCreateView, CalleDeleteView, CalleListView, CalleUpdateView, ProfesionCreateView, ProfesionUpdateView, ProfesionDeleteView, ProfesionListView, NivelEducListView, NivelEducCreateView, NivelEducUpdateView, NivelEducDeleteView, BancoListView, BancoCreateView, BancoUpdateView, BancoDeleteView, CalleListView, CalleCreateView, CalleUpdateView, CalleDeleteView, register
from .views import obtener_informacion_jefe


urlpatterns = [
    path('', views.Bienvenido, name='Bienvenido'),
    path('ListaPersonas', views.ListaPersonas, name='ListaPersonas'),
    path('ListaPersonasEdicion', views.ListaPersonasEdicion, name='ListaPersonasEdicion'),
    path('agregar_persona/', views.agregar_persona, name='agregar_persona'),
    path('cargas_familiares/', views.lista_cargas_familiares, name='lista_cargas_familiares'),
    path('familias/detalle/<int:idfamilia>/', views.detalle_familia, name='detalle_familia'),
    path('ListaPagos', views.ListaPagos, name='ListaPagos'),
    path('actualizacion-de-datos/', views.actualizacion_de_datos, name='ruta_de_actualizacion_de_datos'),
    path('registrar_pagos/', views.registrar_pagos, name='registrar_pagos'),
    path('api/families_count', views.families_count, name='families_count'),
    path('api/residents_count', views.residents_count, name='residents_count'),
    path('api/payments_count', views.payments_count, name='payments_count'),
    path('informes/', views.informes, name='informes'),
    path('editar_persona/<int:persona_idPersona>/', views.editar_persona, name='editar_persona'),
    path('editar_persona_carga/<int:persona_idPersona>/', views.editar_persona_carga, name='editar_persona_carga'),
    path('eliminar_persona/<int:persona_idPersona>/', views.eliminar_persona, name='eliminar_persona'),
    path('detalle_persona/<int:persona_id>/', views.detalle_persona, name='detalle_persona'),
    path('eliminar_pago/<int:pago_id>/', views.eliminar_pago, name='eliminar_pago'),
    path('editar_pago/<int:pago_id>/', views.editar_pago, name='editar_pago'),
    path('eliminar_persona_carga/<int:persona_idPersona>/', views.eliminar_persona_carga, name='eliminar_persona_carga'),
    path('familias/detalle/<int:familia_id>/agregar_persona_carga/', views.agregar_persona_carga, name='agregar_persona_carga'),
    path('seleccionar_bloque/', views.seleccionar_bloque, name='seleccionar_bloque'),
    path('generar_pdf_jefes_familia/<str:selected_bloque>/', views.generar_pdf_jefes_familia, name='generar_pdf_jefes_familia'),
    path('reporte_pagos/', views.reporte_pagos, name='reporte_pagos'),
    path('profesion/', ProfesionListView.as_view(), name='profesion-list'),
    path('profesion/create/', ProfesionCreateView.as_view(), name='profesion-create'),
    path('profesion/update/<int:pk>/', ProfesionUpdateView.as_view(), name='profesion-update'),
    path('profesion/delete/<int:pk>/', ProfesionDeleteView.as_view(), name='profesion-delete'),
    path('nivel_educ/', NivelEducListView.as_view(), name='nivel-educ-list'),
    path('nivel_educ/create/', NivelEducCreateView.as_view(), name='nivel-educ-create'),
    path('nivel_educ/update/<int:pk>/', NivelEducUpdateView.as_view(), name='nivel-educ-update'),
    path('nivel_educ/delete/<int:pk>/', NivelEducDeleteView.as_view(), name='nivel-educ-delete'),
    path('banco/', BancoListView.as_view(), name='banco-list'),
    path('banco/create/', BancoCreateView.as_view(), name='banco-create'),
    path('banco/update/<int:pk>/', BancoUpdateView.as_view(), name='banco-update'),
    path('banco/delete/<int:pk>/', BancoDeleteView.as_view(), name='banco-delete'),
    path('bloque/', views.BloqueListView.as_view(), name='bloque-list'),
    path('bloque/create/', views.BloqueCreateView.as_view(), name='bloque-create'),
    path('bloque/update/<int:pk>/', views.BloqueUpdateView.as_view(), name='bloque-update'),
    path('bloque/delete/<int:pk>/', views.BloqueDeleteView.as_view(), name='bloque-delete'),
    path('calle/', CalleListView.as_view(), name='calle-list'),
    path('calle/create/', CalleCreateView.as_view(), name='calle-create'),
    path('calle/update/<int:pk>/', CalleUpdateView.as_view(), name='calle-update'),
    path('calle/delete/<int:pk>/', CalleDeleteView.as_view(), name='calle-delete'),
    path('salir',views.salir, name='salir'),
    path('register/', views.register, name ='register' ),
    path('permiso-denegado/', views.permiso_denegado, name='PermisoDenegado'),
    path('seleccionar_bloque_carga/', views.seleccionar_bloque_carga, name='seleccionar_bloque_carga'),
    path('generar_pdf_carga_familiar/<str:selected_bloque>/', views.generar_pdf_carga_familiar, name='generar_pdf_carga_familiar'),
    path('reporte_familias/', views.reporte_familias, name='reporte_familias'),
    path('registro/', views.registro , name='registro'),
    path('obtener_informacion_jefe/<int:familia_id>/', obtener_informacion_jefe, name='obtener_informacion_jefe'),
 



]


