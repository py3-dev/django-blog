from django.shortcuts import render
# Create your views here.

posts = [
    {'author':'CoreyMS',
     'title':'Blog Post 1',
     'content':'First post content',
     'date_posted':'July 18, 2023'},
     {'author':'Yash Varshney',
     'title':'Blog Post 2',
     'content':'second post content',
     'date_posted':'January 18, 2021'},
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'Glad to have you!'})