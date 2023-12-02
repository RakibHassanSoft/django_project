from django.shortcuts import render

# F:\Phitron\Django Codes\project_2\templates
def index(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'about.html')