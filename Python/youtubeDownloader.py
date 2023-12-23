import pytube, sys

def getlink():
    link = sys.argv[1]
    yt = pytube.YouTube(link)
    print("Title:", yt.title)

    print("Views:", yt.views)
    yd = yt.streams.get_highest_resolution()

    print(yd.download("C:\\Users\\k7ran\\OneDrive\\Desktop\\Downloaded Youtube Videos"))

    print("Downloaded")

getlink()