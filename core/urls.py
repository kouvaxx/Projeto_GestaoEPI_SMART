from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Auth
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('change-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),

    # Colaboradores
    path('colaboradores/', views.colaborador_list, name='colaborador_list'),
    path('colaboradores/new/', views.colaborador_create, name='colaborador_create'),
    path('colaboradores/edit/<int:pk>/', views.colaborador_update, name='colaborador_update'),
    path('colaboradores/delete/<int:pk>/', views.colaborador_delete, name='colaborador_delete'),

    # Equipamentos
    path('equipamentos/', views.equipamento_list, name='equipamento_list'),
    path('equipamentos/new/', views.equipamento_create, name='equipamento_create'),
    path('equipamentos/edit/<int:pk>/', views.equipamento_update, name='equipamento_update'),
    path('equipamentos/delete/<int:pk>/', views.equipamento_delete, name='equipamento_delete'),

    # Empréstimos
    path('emprestimos/', views.emprestimo_list, name='emprestimo_list'),
    path('emprestimos/new/', views.emprestimo_create, name='emprestimo_create'),
    path('emprestimos/edit/<int:pk>/', views.emprestimo_update, name='emprestimo_update'),
    path('emprestimos/delete/<int:pk>/', views.emprestimo_delete, name='emprestimo_delete'),
    path('emprestimos/devolucao/<int:pk>/', views.emprestimo_devolucao, name='emprestimo_devolucao'),
    # Ajuda
    path('ajuda/', views.ajuda_view, name='ajuda'),
    # Sobre
    path('sobre/', views.sobre_view, name='sobre'),
]
