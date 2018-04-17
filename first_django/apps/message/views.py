from django.shortcuts import render
from .models import UserMessage
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# @csrf_exempt
def get_form(request):
    all_messages=UserMessage.objects.filter(address='北京')
    # all_messages=UserMessage.objects.all()
    for message in all_messages:
        print(message.name)
        message.delete()
        print('delete success')

    if request.method=='POST':
        name=request.POST.get('name','')
        message=request.POST.get('message','')
        address=request.POST.get('address','')
        email=request.POST.get('email','')
        user_message=UserMessage()
        user_message.message=message
        user_message.name=name
        user_message.address=address
        user_message.email=email
        user_message.object_id='123'
        user_message.save()
        print('write success')

    return render(request,'message_form.html')
