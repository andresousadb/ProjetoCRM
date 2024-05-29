# Create your models here.
from django.db import models
from django.contrib.auth.models import User

ESTADO_CIVIL = (
    ('S', 'Solteiro(a)'),
    ('C', 'Casado(a)'),
    ('V', 'Viúvo(a)'),
    ('D', 'Divorciado(a)'),
    ('ND', 'Não Declarar')
)

SEXO = (
    ('F', 'Feminino'),
    ('M', 'Masculino'),
    ('O', 'Outros')
)

CIDADE = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

CONVIDOU = (
    ('S', 'Sim'),
    ('N', 'Não')
)

class Record(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11,blank=True)
    endereco = models.CharField(max_length=300)
    cidade = models.CharField(max_length=100,choices=CIDADE)
    cep = models.CharField(max_length=200, blank=True)
    sexo = models.CharField(max_length=1,choices=SEXO, blank=True)
    status_civil = models.CharField(max_length=2, choices=ESTADO_CIVIL, blank=True)
    dt_nascimento = models.DateField()
    convite = models.CharField(max_length=1,choices=CONVIDOU)
    convidou = models.CharField(max_length=200,blank=True)

    def __str__(self):

        return self.sobrenome + "   " + self.nome










