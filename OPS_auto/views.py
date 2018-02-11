from django.shortcuts import render
from OPS_auto.scripts import getinfo
# Create your views here.

def index(request):
    t=getinfo.getMemCpu()
    title="hello"
    content = {"content":"凤凤和阳阳，新年快乐!","title":title}
    return render(request,'OPS_auto/index.html' ,content)

i = 1
count = 0
while 1:
    if i % 2 == 0 or i % 3 == 0:
        count += 1
        if count == 2333:
            print(i)
            break

    i += 1


