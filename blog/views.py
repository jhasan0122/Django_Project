from django.shortcuts import render
from .models import Post


# posts = [
#     {
#         "author":"Jehan",
#         "title":"Blog Post 1",
#         "content":"First post conetent",
#         "date_posted":"August 27, 2018"
#     },
#     {
#         "author":"Hasan",
#         "title":"Blog Post 2",
#         "content":"Second post conetent",
#         "date_posted":"August 28, 2018"
#     }
# ]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
