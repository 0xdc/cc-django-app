from django.apps import AppConfig


class {{ cookiecutter.name | capitalize }}Config(AppConfig):
    name = '{{ cookiecutter.name }}'
