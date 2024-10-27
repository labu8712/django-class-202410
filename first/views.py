from django.http import HttpResponse


def message_view(request):
    return HttpResponse("Hello!!!")


def say_hello(request):
    get_parms = request.GET  # 透過 Http 傳遞進來的 GET 參數
    name = get_parms.get("name", "unknown")  # 從 GET 參數（dict）中尋找 name 的值
    return HttpResponse(f"Hello {name}")
