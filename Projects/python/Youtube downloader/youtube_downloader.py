import yt_dlp #using yt_dlp since pytube is not updated

save_path = "" #place download path
link = input("Paste the YouTube link of the video you would like to download:\n")

try:
    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:   #Get metadata
        info = ydl.extract_info(link, download=False)
        title = info.get("title", "Unknown Video")
    choice = input(f"You're about to download the following video:\nTitle: {title}\nPress Enter to continue or type 'stop' to cancel: ")
    if choice.lower() == "stop":
        print("Download cancelled.")
        exit()
    ydl_opts = {
        "format": "18",  #MP4 format
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",
        "quiet": True,
        "progress_hooks": [lambda d: print("Downloading is in progress... Please wait.")]
    }
    print("Let's go!!...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Video downloaded successfully!")

except:
    print("There was an error, video not downloaded!")
print("Press enter to exit program.")
