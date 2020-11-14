from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    count = request.session.get('count', 0) + 1
    if count > 4:
        count = 0
    request.session['count'] = count
    response = HttpResponse(f'view_count={count}')
    response.set_cookie('dj4e_cookie', 'eed4435e', max_age=1000)
    return response
