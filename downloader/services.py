import yt_dlp


def format_size(size):
    if not size:
        return "Unknown"
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"

def get_clean_formats(formats):

    clean_formats = []
    seen = set()

    for fmt in formats:

        resolution = fmt.get("resolution")
        ext = fmt.get("ext")
        format_id = fmt.get("format_id")

        if format_id.startswith("hls"):
            continue

        if format_id.startswith("dash"):
            continue

        if ext not in ["mp4", "m4a"]:
            continue

        key = (resolution, ext)

        if key in seen:
            continue

        seen.add(key)

        clean_formats.append({
            "format_id": format_id,
            "resolution": resolution,
            "ext": ext,
           "filesize": format_size(fmt.get("filesize"))
        })

    return clean_formats

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
        "formats": get_clean_formats(
        info.get("formats", [])
        )
    }