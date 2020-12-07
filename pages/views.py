from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Page
# Create your views here.


def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.body_text,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    # assert False
    # return HttpResponse("<h1>The Meandco Homepage</h1>")
    return render(request, 'pages/page.html', context)
