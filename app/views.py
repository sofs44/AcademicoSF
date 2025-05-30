from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .models import Pessoa


# Página inicial
class IndexView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'index.html', {'pessoas': pessoas})

# Gerenciar pessoas
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

# Gerenciar ocupações
class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacoes.html', {'ocupacoes': ocupacoes})

# Gerenciar instituições de ensino
class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituiçoes_de_ensino.html', {'instituicoes': instituicoes})

# Gerenciar áreas do saber
class AreasSaberView(View):
    def get(self, request, *args, **kwargs):
        areas_saber = AreaSaber.objects.all()
        return render(request, 'areas_do_saber.html', {'areas_saber': areas_saber})

# Gerenciar cursos
class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

# Gerenciar turmas
class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})

# Gerenciar disciplinas
class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

# Gerenciar matrículas
class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

# Gerenciar avaliações
class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

# Gerenciar frequência
class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias})

# Gerenciar turnos
class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turnos.objects.all()
        return render(request, 'turnos.html', {'turnos': turnos})

# Gerenciar cidades
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

# Gerenciar ocorrências
class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

# Gerenciar disciplinas por cursos
class CursoDisciplinasView(View):
    def get(self, request, *args, **kwargs):
        curso_disciplinas = CursoDisciplina.objects.all()
        return render(request, 'cursos_disciplinas.html', {'cursos_disciplinas': curso_disciplinas})

# Gerenciar tipos de avaliação
class AvaliacaoTiposView(View):
    def get(self, request, *args, **kwargs):
        avaliacao_tipos = AvaliacaoTipo.objects.all()
        return render(request, 'tipo_de_avaliaçao.html', {'avaliacao_tipos': avaliacao_tipos})

class DeletePessoaView(View):
    def get(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)
        pessoa.delete()
        messages.success(request, 'Pessoa excluída com sucesso!')
        return redirect('index')  # Redireciona para a página inicia