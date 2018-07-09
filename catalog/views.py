from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from catalog.models import Article
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods
import datetime


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    current_time = datetime.date.today().isoformat()
    return HttpResponse(current_time, content_type='text/plain')


@require_http_methods(['GET', 'POST'])  # not sure how to use it yet
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


def handler400(request, *args, **kwargs):
    return HttpResponse('Неизвестная операция или деление на ноль', status=400)


def articles_redirect(request):
    return redirect('articles_detail', id=10)


@require_http_methods(['GET'])
def calculate(request):
    operation = request.GET['op']
    left_oparand = int(request.GET['left'])
    right_operand = int(request.GET['right'])
    print(request.GET, operation, left_oparand, right_operand)
    if operation == '+' or ' ':
        result = left_oparand + right_operand
    elif operation == '-':
        result = left_oparand - right_operand
    elif operation == '*':
        result = left_oparand * right_operand
    elif operation == '/' and right_operand != 0:
        result = left_oparand / right_operand
    else:
        return handler400(request)
    return HttpResponse(result)
