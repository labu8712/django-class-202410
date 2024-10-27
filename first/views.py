from django.http import HttpResponse


def message_view(request):
    return HttpResponse("Hello!!!")
