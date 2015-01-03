from django.shortcuts import render
from django.templatetags.static import static as static_url


def home(request):
    return render(request, 'base.html')


def tests(request):
    return render(request, 'qunit.html', dict(
        title='Mist Studio Unit Tests',
        tests_url=static_url('tests/studio.js'),
    ))