from django.http import HttpResponse

def index(request):
    return HttpResponse("Testing testing 1 2 3, Houston we have a problem...")
