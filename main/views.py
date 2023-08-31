from django.http import HttpResponse
from . import tasks


def home(request):
    tasks.download_a_cat.delay()
    return HttpResponse("<h1> Гружу кота!!!! </h1>")
