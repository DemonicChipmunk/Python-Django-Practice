from django.shortcuts import render

posts = [

    {
        'author' : 'CoreyMs',
        'title'  : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'August, 27, 2020'
    },

    {
        'author' : 'Jane Doe',
        'title'  : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'August, 29, 2020'
    }

]


def home(requests) :
    context = {
        'posts' : posts
    }
    return render(requests, 'blog/home.html', context)

def about(requests) :
    return render(requests, 'blog/about.html')
# Create your views here.
