from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text':'hello world','number':'5'}
    return render(request,'basic_app/index.html',context=context_dict)

def other(request):
    return render(request,'basic_app/other.html')
def base(request):
    return render(request,'basic_app/base.html')
def relative_url_templates(request):
    return render(request,'basic_app/relative_url_templates.html')
