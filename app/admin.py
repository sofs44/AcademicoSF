from django.contrib import admin
from .models import *

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
