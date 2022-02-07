#사용자정의
from django.contrib.auth.models import User
#장고의 사용자 모듈


# 장고의 view를 html문법으로 바꾸기 위한 렌더링모듈 과 new_topic view가 home으로 돌아가기 위한 redirect모듈
from django.shortcuts import render, redirect


from  .models import Topic, Reply
# 모델의 클래스명

from django.http import HttpResponse

from django import forms


from .forms import CreateTopic

# 추가하기
def home(request):
    topics = Topic.objects.all()   #models의 Topic 개체 생성
    return render(request,'home.html',{'topics':topics})
 
def new_topic(request):

    topics = Topic.objects.all()
    if request.method =='POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            subject=subject,
            message=message,
            writter=user
        )

        post = Reply.objects.create(
            message=message,
            created_by=user

        )

        return redirect('home')
  
       
    
    return render(request,'new_topic.html',{'topics':topics})



