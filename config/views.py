from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# views는 두뇌다 , Create your views here.
def home(request): # request 파라미터 필수 !
    return HttpResponse("<h1>Home</h1>")

#Json 1개 짜리
def dictway(request):
    return JsonResponse(
        {
            'key2' : 'value2',
            'key' : 'value',
        }
    )
#Json 여러개
def listway(request):
    
    return JsonResponse(
        [
            {
                'key' : 'value'
            },
            {
                'key2' : 'value2'
            },
        ], safe=False  # dictionary가 아닌 list와 같은 형태 사용시 반드시 해줘야함
        )

def root(request):

    return HttpResponse("<h1>THANK U EOT</h1>")
