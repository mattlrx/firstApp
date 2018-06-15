from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
import serial
import time

# Create your views here.

def index(request):
    #ser = serial.Serial('/dev/ttyACM0',9600)
    #time.sleep(2)
    #ser.write(b'0')

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))

    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = " You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)




