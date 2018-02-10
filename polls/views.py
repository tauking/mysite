from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils import timezone
from polls.scripts import getsum


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def info(request):
    user=request.POST["user"]
    try:
        users = getsum.sssum(int(user))
    except:
        users="不是合法内容"
    return HttpResponse(users)

def homepage(request):
    now=str(timezone.now())
    content={'now':now}
    return render(request,'polls/index.html' ,content)
