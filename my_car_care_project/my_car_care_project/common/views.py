from django.shortcuts import render
from django.views import generic as views


class IndexView(views.TemplateView):
    template_name = 'common/index.html'


def learn_more_view(request):
    return render(request, 'common/learn_more.html')


def about_us_view(request):
    return render(request, 'common/about_us.html')
