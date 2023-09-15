from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
#from initialization import bot
from .forms import FileUploadForm
from .tools.fileReader import read_files
import sys
sys.path.append('/home/vcp/demo/demo1/')
from apps import bot
# Create your views here.


def test():
    return HttpResponse("test")


def upload_files(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            read_files(request.FILES.getlist('files'))
        messages.success(request, 'File uploaded successfully')
    else:
        form = FileUploadForm()

    return render(request, 'upload.html', {'form': form})


def chat_bot(request):
    return render(request, "chat_bot.html")


def chat_bot_response(request):
    if request.method == "POST":
        ##########get userInput from front##############
        query = request.body.decode('utf-8')
        return HttpResponse(bot.react(query))


def home(request):
    return render(request, "home.html")
