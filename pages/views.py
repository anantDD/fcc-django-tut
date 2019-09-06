from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request):
    # string of HTML code, not actual HTML code
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request):
    return render(request, "contact.html", {})


def about_view(request):
    my_context = {
        "my_text": "This is coming from context",
        "my_number": 123,
        "my_list": ['asdf', 'xyz', 'def', 'non', 4],
        "my_html": "<h1>hello world</h1>"
    }
    return render(request, "about.html", my_context)
