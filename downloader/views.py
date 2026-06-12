from django.shortcuts import render


def home(request):

    url = None

    if request.method == "POST":
        url = request.POST.get("url")

    return render(
        request,
        "home.html",
        {
            "url": url
        }
    )