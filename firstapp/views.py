from django.shortcuts import render
from django.http import HttpResponse

# views는 두뇌다 , Create your views here.
def index1(request): # request 파라미터 필수 !
    return HttpResponse("<u>Hello</u>")

def index2(request): # request 파라미터 필수 !
    return HttpResponse("<u>Hi</u>")

def main(request): # request 파라미터 필수 !
    return HttpResponse("<u>Main</u>")

from .models import Curriculum, Person

def insert(request): # request 파라미터 필수 !
    Curriculum.objects.create(name='linux')

    c = Curriculum(name='django')
    c.save()

    return HttpResponse("데이터 입력완료")

def show(request):
    curriculum = Curriculum.objects.all()
    print(curriculum)
    context = {
        'data' : curriculum
    }

    return render(request,'firstapp/show.html', context)

    # result= ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)

def person_add(request):
    p1 = Person(name="Fred Flinstone", shirt_size="L")
    p2 = Person(name="Fred Flinstone", shirt_size="M")
    p3 = Person(name="Fred Flinstone", shirt_size="S")
    p1.save()
    p2.save()
    p3.save()
    return HttpResponse('<h2>Done!</h2>')

def person(request):
    per = Person.objects.all()
    #print(per)
    context = {
        'data' : per
    }
    return render(request, 'firstapp/person.html', context)
