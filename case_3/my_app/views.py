
from django.shortcuts import render, redirect
from .forms import NameForm
from .models import Name
from django.http import HttpResponse


def main(request):
    name = request.GET.get('name', 'Гость')
    context = {'name': name}
    return render(request, 'my_app/main.html', context)


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            return hello(request, visitor.name)
    else:
        form = NameForm()

    return render(request, 'my_app/index.html', {'form': form})


def hello(request, name):
    return render(request, 'my_app/main.html', {'name': name})


def page_forbidden(request, exception=None):
    return render(request, 'errors/403.html', status=403)


def page_not_found(request, exception=None):
    return render(request, 'errors/404.html', status=404)


def server_error(request):
    return render(request, 'errors/500.html', status=500)

