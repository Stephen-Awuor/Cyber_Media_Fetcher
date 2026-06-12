from django.shortcuts import render
from django.http import HttpResponse
import yt_dlp


def home(request):
    video = None
    error = None
    if request.method == "POST":
        url = request.POST.get("url")
        try:
            ydl_opts = {
                "quiet": True,
                "noplaylist": True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(
                    url,
                    download=False
                )
            video = {
    "url": url,
    "title": info.get("title"),
    "thumbnail": info.get("thumbnail"),
    "uploader": info.get("uploader"),
    "duration": info.get("duration"),
    "formats": info.get("formats", [])
}
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

    url = request.GET.get("url")
    format_id = request.GET.get("format")

    return HttpResponse(
        f"Download requested: {format_id}"
    )