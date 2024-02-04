from pytube import YouTube


try:
    
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    print("Title:", yt.title)
    print("Views:", yt.views)

    # highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the current directory
    yd.download()
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))