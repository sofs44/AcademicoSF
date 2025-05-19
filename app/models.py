from django.db import models

# Classe base Pessoa
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai", null=True, blank=True)
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe", null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    cidade = models.ForeignKey('Cidade', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cidade")
    ocupacao = models.ForeignKey('Ocupacao', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ocupação")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoa"
    
# Classe Cidade
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    
    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

# Classe Ocupacao
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

# Classe InstituicaoEnsino
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição de ensino")
    site = models.URLField(verbose_name="Site da instituição")
    telefone = models.CharField(max_length=15, verbose_name="Telefone", null=True, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cidade")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

# Classe AreaSaber
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do saber")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"

# Classe Curso
class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga horária total")
    duracao_meses = models.IntegerField(verbose_name="Duração em meses")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de ensino")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

# Classe Turma
class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

# Classe Disciplina
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

# Classe Matricula
class Matricula(models.Model):
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de ensino")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_previsao_termino = models.DateField(verbose_name="Data de término prevista")
    
    def __str__(self):
        return f'Matrícula de {self.pessoa.nome} no curso {self.curso.nome}'

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

# Classe Avaliacao
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da avaliação")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    avaliacao_tipo = models.ForeignKey('AvaliacaoTipo', on_delete=models.CASCADE, verbose_name="Tipo de Avaliação")
    
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

# Classe AvaliacaoTipo
class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do tipo de avaliação")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"

# Classe Frequencia
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de faltas")
    
    def __str__(self):
        return f'{self.pessoa.nome} - {self.disciplina.nome}'

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

# Classe Turnos
class Turnos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do turno")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

# Classe Ocorrencia
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição da ocorrência")
    data_ocorrencia = models.DateField(verbose_name="Data da ocorrência")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa envolvida")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso associado", null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina associada", null=True, blank=True)
    
    def __str__(self):
        return f"Ocorrência de {self.pessoa.nome} - {self.descricao}"
    
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


# Classe CursoDisciplina
class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.IntegerField(verbose_name="Carga horária da disciplina no curso")
    
    def __str__(self):
        return f"{self.curso.nome} - {self.disciplina.nome}"
    
    class Meta:
        verbose_name = "Curso e Disciplina"
        verbose_name_plural = "Cursos e Disciplinas"

