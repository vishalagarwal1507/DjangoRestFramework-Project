from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.



def api_home(request):
    return JsonResponse({"message":"Django First view"})
