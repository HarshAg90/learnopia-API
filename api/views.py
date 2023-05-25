from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Entity
from django.http import JsonResponse

# Create your views here.
def home(request):

    for i in range(5):
        post = Entity(type="image field", by_user="harsh",cource="BCA",sem="4",topic=["AI","ML"], image_index=None,embed_url=None,content_heading="example content", content_body= "body", redirect_link= "none")
        post.save()
    
    posts=Entity.objects.all()
    print(posts)
    return JsonResponse({
        "Success": "true"
    })

def error_view():
    return JsonResponse({
        "status":"not found",
        "Description":"endpoint doesnt exist"
    })