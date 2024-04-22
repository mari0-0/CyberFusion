from django.shortcuts import render, redirect
from .models import Command, Output, IpAddress
from django.http import JsonResponse
from .forms import UsernameForm, PasswordForm
from django.views.decorators.csrf import csrf_exempt
from .tasks import runCyberFusion

# Create your views here.
#celery -A cyberfusion.celery worker -l info
# pip install eventlet
# celery -A cyberfusion.celery worker -l info -P eventlet
def index(request):

    runCyberFusion.delay()
    return render(request,'form.html')

########## IP ##############
def save_ip(request):

    if request.method == "POST":
        i = request.POST.get('input_data')
        if i:
            ip = IpAddress.objects.create(ip = i)
            ip.save()
            return redirect('usernames')
    return render(request,'base.html')

def get_ip(request):
    ip = IpAddress.objects.all().last()
    data = {'ip': 'NoIpFound'}
    if ip:
        data = {'ip': f'{ip.ip}'}
    return JsonResponse(data)

def faq(request):
    return render(request, "faq.html")    

def editor1(request):
    if request.method == 'POST':
        form1 = UsernameForm(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['body']
            usernames = username.replace("<p>","").replace("</p>","").replace("<br />","").split("\n\n")
            with open("usernames.txt", 'w') as file:
                for username in usernames:
                    file.write(username)
            return redirect('passwords')
    form1 = UsernameForm()
    return render(request, "editor.html", {'form1': form1, 'username': True})   
 
def editor2(request):
    if request.method == 'POST':
        form1 = PasswordForm(request.POST)
        if form1.is_valid():
            password = form1.cleaned_data['body']
            passwords = password.replace("<p>","").replace("</p>","").replace("<br />","").split("\n\n")
            with open("passwords.txt", 'w') as file:
                for password in passwords:
                    file.write(password)
            return redirect('index')
    form1 = PasswordForm()
    return render(request, "editor.html", {'form1': form1})    
########## COMMAND ##############

def save_command(request):
    c = request.GET.get('command')
    if c:
        cmd = Command.objects.create(command = c)
        cmd.save()
        return JsonResponse({"message": "command sent sucessfully"})
    return JsonResponse({"error": "command not in data"})


def get_command(request):
    try:
        cmd = Command.objects.all()[0]
        command = cmd.command
        data = {'command': f'{command}'}
        cmd.delete()
        return JsonResponse(data)
    except:
        return JsonResponse({'command': "ErrorNoCommand"})


########## OUTPUT ##############

@csrf_exempt
def send_output(request):
    if request.method == 'POST':
        output = request.POST.get('output')
        if output:
            op = Output.objects.create(output=output)
            op.save()
            return JsonResponse({'message': 'output sent!'})
        return JsonResponse({'error': 'Blank message sent'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
    
def get_output(request):
    try:
        op = Output.objects.all().first()
        output = op.output
        data = {'output': f'{output}'}
        op.delete()
        return JsonResponse(data)
    except:
        return JsonResponse({'output': "ErrorNoOutput"})
