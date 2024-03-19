from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

def wine(request):

    file_data = open("SPIKEDWINE/files/test.zip", 'rb').read()

    response = HttpResponse(file_data)
    response['Content-Type'] = 'application/x-zip-compressed'
    response['Content-Disposition'] = 'attachment; filename=payload.zip'

    return response

