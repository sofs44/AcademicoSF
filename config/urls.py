from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('delete/<int:id>/', DeletePessoaView.as_view(), name='delete_pessoa'),
    
    # Gerenciar pessoas
    path('pessoa.html', PessoasView.as_view(), name='pessoa'),
    
    # Gerenciar ocupações de pessoas
    path('ocupacoes.html', OcupacoesView.as_view(), name='ocupacao'),
    
    # Gerenciar instituições de ensino
    path('instituiçoes_de_ensino.html', InstituicoesView.as_view(), name='instituicao'),
    
    # Gerenciar áreas do saber
    path('areas_do_saber.html', AreasSaberView.as_view(), name='area_saber'),
    
    # Gerenciar cursos
    path('cursos.html', CursosView.as_view(), name='curso'),
    
    # Gerenciar turmas
    path('turmas.html', TurmasView.as_view(), name='turma'),
    
    # Gerenciar disciplinas
    path('disciplinas.html', DisciplinasView.as_view(), name='disciplina'),
    
    # Gerenciar matrículas
    path('matricula.html', MatriculasView.as_view(), name='matricula'),
    
    # Gerenciar avaliações
    path('avaliacoes.html', AvaliacoesView.as_view(), name='avaliacao'),
    
    # Gerenciar frequência
    path('frequencias.html', FrequenciasView.as_view(), name='frequencia'),
    
    # Gerenciar turnos
    path('turnos.html', TurnosView.as_view(), name='turno'),
    
    # Gerenciar cidades
    path('cidades.html', CidadesView.as_view(), name='cidade'),
    
    # Gerenciar ocorrências / advertências
    path('ocorrencias.html', OcorrenciasView.as_view(), name='ocorrencia'),
    
    # Gerenciar disciplinas por cursos
    path('cursos_disciplinas.html', CursoDisciplinasView.as_view(), name='curso_disciplinas'),
    
    # Gerenciar tipos de avaliação
    path('tipo_de_avaliaçao.html', AvaliacaoTiposView.as_view(), name='avaliacao_tipo'),

]
