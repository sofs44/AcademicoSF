from django.contrib import admin
from .models import *

#inline de frequência em Pessoa
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [FrequenciaInline]

admin.site.register(Frequencia)
admin.site.register(Pessoa,PessoaAdmin)


# Registro das models no admin
admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(AvaliacaoTipo)
admin.site.register(Frequencia)
admin.site.register(Turnos)
admin.site.register(Pessoa)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
