try:
    from django.urls import include, path
except ImportError:
    from django.conf.urls import include
    from django.conf.urls import url as path

urlpatterns = [
    path(r'', include('{{ cookiecutter.name }}.urls', namespace='{{ cookiecutter.name }}'),
]
