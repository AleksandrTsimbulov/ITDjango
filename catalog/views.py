from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from catalog.models import Article
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles': articles,
    }, content_type='text/plain')


@require_http_methods(['GET', 'POST']) # not sure how to use it yet
def articles_list(request):
    print(request.GET.getlist('name'))
    return HttpResponse('Список статей')


def articles_detail(request, id):
    if 'name' in request.GET:
        request.session['name'] = request.GET['name']
    name = request.session.get('name', 'Anonymous')
    print(request.META)
    url = reverse('articles_detail', kwargs={'id': 17})
    return HttpResponse(f'Статья {id}: {url} [{name}]')


def handler404(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse('Не найдено', status=404)


def articles_redirect(request):
    return redirect('articles_detail', id=10)
