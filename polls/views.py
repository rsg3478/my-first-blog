from django.http import HttpResponse 

def index(request): 
    return HttpResponse("설문조사의 인덱스 위치 입니다.")
