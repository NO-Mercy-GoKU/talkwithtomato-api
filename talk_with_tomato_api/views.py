from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import bot
from . import msg_id
import datetime



def home(request):
    return HttpResponse('<title>TalkWithTomato-API</title><head><b><Strong>Hello Developers! Welcome to Tomato.</strong></b></head><br><br><br><br><head><b>Guidelines</b></head><br><br><body>This is a chatbot <b>API</b> which can communicate through <b>requests</b>. The response will be in <b>Json format</b> which will contain <b>"reply" key</b> with your answer as the value.<br>Request a <b>POST</b> method at <b>"reply/"</b> with <b>"body"</b> key and the question as the value in your data.<br>You can use this API for <b>free</b> in your any code of any language.<br><br><br><br><br>The frontend and sample codes are coming soon...<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center>Developed by MahaKAAL (2020)</center></body>')

@csrf_exempt
def reply(request):
    global msg_id
    dt=datetime.datetime.now()
    question='Question is not found'
    if request.method == 'POST':
        if 'body' in request.POST:
            question = str(request.POST['body'])
            temp_msg_id=msg_id+1
            answer=str(bot.get_response(str(question)))
            msg_id+=1

        else:
            answer = "Please provide a 'body' parameter with your question."
            temp_msg_id=None
        result = json.dumps({'question':question,'ans':answer, 'msg_id':temp_msg_id, 'date':str(dt.date()), 'time':str(dt.time())[:-7]})
        return HttpResponse(result)
    else:
        return HttpResponse('<title>TalkWithTomato-API</title><head><b><Strong>Hello Developers! Welcome to Tomato.</strong></b></head><br><br><br><br><head><b>Guidelines</b></head><br><br><body>This is a chatbot <b>API</b> which can communicate through <b>requests</b>. The response will be in <b>Json format</b> which will contain <b>"reply" key</b> with your answer as the value.<br>Request a <b>POST</b> method at <b>"reply/"</b> with <b>"body"</b> key and the question as the value in your data.<br>You can use this API for <b>free</b> in your any code of any language.<br><br><br><br><br>The frontend and sample codes are coming soon...<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center>Developed by MahaKAAL (2020)</center></body>')