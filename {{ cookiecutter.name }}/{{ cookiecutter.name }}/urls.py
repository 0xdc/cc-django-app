try:
    from django.urls import path
except ImportError:
    from django.conf.urls import url as path

from . import views

app_name = "{{ cookiecutter.name }}"
urlpatterns = [
    #path(r'/?', views., name=""),
]
