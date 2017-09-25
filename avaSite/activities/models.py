from django.db import models
from django.conf import settings
from django.utils import timezone


#Atividade 1: O professor pode cadastrar uma imagem e um audio e o aluno deve retornar um texto '''
# class VerEscutarEscrever(models.Model):
#     name = models.CharField('Nome:', max_length=100)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, verbose_name='Usuário',
#     )
#     slug = models.SlugField('Atalho')
#     description = models.TextField('Descrição da atividade', blank=True)
#     image = models.ImageField(
#         upload_to='activities/images', verbose_name='Imagem',
#         null=True, blank=True
#     )
#     created_at = models.DateTimeField('Criado em', auto_now_add=True)

#     def __str__(self):
#             return self.name
#     @models.permalink
#     def get_absolute_url(self):
#         return ('activities:details', (), {'slug': self.slug})

#     class Meta:
#         verbose_name = 'Atividade'
#         verbose_name_plural = 'Atividades'
#         ordering = ['name']
# Atividade 2: O professor pode cadastrar uma imagem e um texto e o aluno deve retornar um audio '''

# Atividade 3: O professor pode cadastrar um audio e um texto e o aluno deve retornar uma imagem'''