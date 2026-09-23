from django.urls import path
from . import views

urlpatterns = [
    # A página inicial agora é a lista de tarefas do CRUD
    path('', views.TarefaListView.as_view(), name='lista_tarefas'),
    
    # Demais rotas do CRUD (sem a palavra 'tarefas/')
    path('nova/', views.TarefaCreateView.as_view(), name='cria_tarefa'),
    path('<int:pk>/', views.TarefaDetailView.as_view(), name='detalhe_tarefa'),
    path('<int:pk>/editar/', views.TarefaUpdateView.as_view(), name='edita_tarefa'),
    path('<int:pk>/deletar/', views.TarefaDeleteView.as_view(), name='deleta_tarefa'),
]