from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import datetime

# Importando o seu modelo tarefa
from .models import tarefa

def home(request):
    data_atual = datetime.datetime.now()
    return render(request, 'lista.html', {'data_atual': data_atual})



class TarefaListView(ListView):
    model = tarefa
    template_name = 'lista_tarefas.html' 
    context_object_name = 'tarefas' 

class TarefaDetailView(DetailView):
    model = tarefa
    template_name = 'detalhe_tarefa.html'


class TarefaCreateView(CreateView):
    model = tarefa
    template_name = 'form_tarefa.html'
    fields = ['titulo', 'descricao', 'concluida'] 
    success_url = reverse_lazy('lista_tarefas') 

class TarefaUpdateView(UpdateView):
    model = tarefa
    template_name = 'form_tarefa.html'
    fields = ['titulo', 'descricao', 'concluida']
    success_url = reverse_lazy('lista_tarefas')


class TarefaDeleteView(DeleteView):
    model = tarefa
    template_name = 'deleta_tarefa.html'
    success_url = reverse_lazy('lista_tarefas')



