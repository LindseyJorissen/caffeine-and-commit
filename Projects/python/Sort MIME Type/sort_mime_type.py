def get_extension(filename):
    dot_index = filename.rfind(".")
    if dot_index == -1:
        return ""
    return filename[dot_index:].lower()

def get_mime_type(filename):
    ext = get_extension(filename)
    match ext:
        case ".jpg" | ".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".gif":
            return "image/gif"
        case ".mp4":
            return "video/mp4"
        case ".mp3":
            return "audio/mpeg"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

filename = input("File name: ").strip()
print(get_mime_type(filename))
