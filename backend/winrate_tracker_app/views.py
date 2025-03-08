from django.http import HttpResponse, JsonResponse
from winrate_tracker_app.src import dummy as wt
import datetime

def ping_frontend(request):
    return JsonResponse({
        "ts": f"{datetime.datetime.now()}",
        "message": "Hello from Django!"
    })

def index(request):
    return HttpResponse("Hello, world. You're at the TRACKER PAGE.")

def someView(request):
    result = wt.test("my message")
    return HttpResponse(f"{result}")