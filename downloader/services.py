import yt_dlp
def get_video_info(url):
    ydl_opts = {
        "quiet": True,
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
            url,
            download=False
        )
    return {
        "url": url,
        "title": info.get("title"),
        "thumbnail": info.get("thumbnail"),
        "uploader": info.get("uploader"),
        "duration": info.get("duration"),
        "formats": info.get("formats", [])
    }