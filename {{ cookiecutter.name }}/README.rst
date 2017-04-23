{{ cookiecutter.name }}
====

Quick start
-----------

1. Add "{{ cookiecutter.name }}" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        '{{ cookiecutter.name }}',
    ]

2. Include the {{ cookiecutter.name }} URLconf in your project urls.py like this::

    url(r'^{{ cookiecutter.name }}/', include('{{ cookiecutter.name }}.urls')),

3. Run `python manage.py migrate` to create the {{ cookiecutter.name }} models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/{{ cookiecutter.name }}/ to view templates.
