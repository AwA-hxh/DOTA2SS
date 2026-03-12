from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
        'current_page': 'home'
    })

def home_test(request):
    panel = request.GET.get("panel", "mocktrade")

    return render(request, "hometesting.html", {
        "panel": panel
    })