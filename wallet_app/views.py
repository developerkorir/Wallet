from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def contact(request):
    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')


def how_it_works(request):
    return render(request, 'how-it-works.html')


def legal(request):
    return render(request, 'legal.html')


def privacy_policy(request):
    return render(request, 'privacy-policy.html')


def service_details(request):
    return render(request, 'service-details.html')


def services(request):
    return render(request, 'services.html')


def terms(request):
    return render(request, 'terms.html')