import pytube, sys

def getlink():
    link = sys.argv[1]
    yt = pytube.YouTube(link)
    print("Title:", yt.title)

    print("Views:", yt.views)
    correct = input("Is that the right video? ")

    if correct == 'yes':
        yd = yt.streams.get_highest_resolution()

        yd.download("C:\\Users\\k7ran\\Desktop\\Downloaded Youtube Videos")

    print("Downloaded")

getlink()