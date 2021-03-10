from django.shortcuts import render

# Create your views here.
# render the index.html, where react will take control 
def index(request,*args, **kwargs):
    return render(request,'frontend/index.html')
