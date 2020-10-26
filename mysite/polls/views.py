from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 0ed8861d is the polls index.")
