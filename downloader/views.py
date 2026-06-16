from django.shortcuts import render
from .services import get_video_info
from django.http import HttpResponse


def home(request):

    video = None
    error = None

    if request.method == "POST":

        url = request.POST.get("url")

        try:
            video = get_video_info(url)

        except Exception as e:
            error = str(e)

    return render(
        request,
        "home.html",
        {
            "video": video,
            "error": error
        }
    )

def download(request):
    return HttpResponse("Download feature coming soon")