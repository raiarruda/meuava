from django.conf.urls import include, url
import django.contrib.auth.views

from datetime import datetime
from . import views
from . import forms

urlpatterns = [
    url(r'^$', views.dashboard, 
        name='dashboard'),


    url(r'^entrar/$', django.contrib.auth.views.login, 
        {'template_name': 'accounts/login.html',
      #   'authentication_form': forms.BootstrapAuthenticationForm,
         'extra_context':
         {
                'title': 'Entrar',
                'year': datetime.now().year,
            },
          
        },
        name='login'),

    url(r'^sair/$', django.contrib.auth.views.logout, 
        {'next_page': 'core:home'}, name='logout'),


    url(r'^cadastre-se/$', views.register, 
        name='register'),
    url(r'^editar/$', views.edit, 
        name='edit'),
    url(r'^editar-senha/$', views.edit_password, 
        name='edit_password'),
]