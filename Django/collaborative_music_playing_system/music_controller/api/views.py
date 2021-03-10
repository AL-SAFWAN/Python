from django.shortcuts import render
from django.http import HttpResponse
# Create your endpoints here

def main(request):
    return  HttpResponse('hello')
