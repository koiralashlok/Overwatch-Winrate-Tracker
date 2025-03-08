from django.http import HttpResponse, JsonResponse
from winrate_tracker_app.src import dummy as wt
import datetime

def ping_frontend(request, id):
    if id:
        return JsonResponse({
            "ts": f"{datetime.datetime.now()}",
            "message": f"Hello {id} from Django!"
        })
    return HttpResponse("You have found an endpoint not a webpage yippee.")

def index(request):
    return HttpResponse("Hello, world. You're at the TRACKER PAGE.")

def someView(request):
    result = wt.test("my message")
    return HttpResponse(f"{result}")