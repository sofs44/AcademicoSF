from django.contrib import admin
from .models import *

class PessoaInlineOcupacao(admin.TabularInline):
    model = Pessoa  # Pessoa deve ter FK para Ocupacao
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInlineOcupacao]

admin.site.register(Ocupacao, OcupacaoAdmin)

class CursoInline(admin.TabularInline):
    model = Curso  # Curso deve ter FK para InstituicaoEnsino
    extra = 1

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)

class CursoInlineArea(admin.TabularInline):
    model = Curso  # Curso deve ter FK para AreaSaber
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInlineArea]

admin.site.register(AreaSaber, AreaSaberAdmin)

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao  # Avaliacao deve ter FK para Disciplina
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

admin.site.register(Disciplina, DisciplinaAdmin)


# Registro das models que não precisam de inlines
admin.site.register(Cidade)
admin.site.register(Matricula)
admin.site.register(AvaliacaoTipo)
admin.site.register(Frequencia)
admin.site.register(Turnos)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(Turma)
admin.site.register(Avaliacao)  # Se quiser registrar também sem inline
admin.site.register(Curso)
admin.site.register(Pessoa)