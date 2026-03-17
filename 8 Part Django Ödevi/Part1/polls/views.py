from django.http import HttpResponse


def index(request):
    return HttpResponse("Merhaba, dünya. Ana sayfa böyle.")
