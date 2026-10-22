from django.http import JsonResponse, HttpResponse
from django.db import connection

def db_version(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
    return JsonResponse({'version': version})

def home(request):
    return HttpResponse("<h1>Nothing to show here</h1>")