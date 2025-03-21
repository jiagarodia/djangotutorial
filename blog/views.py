from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post1',
        'content':'First post content',
        'date_posted':'Aug 21, 2018'
    }
]

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
