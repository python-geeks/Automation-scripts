from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format': 'bestaudio'})

while True:

    try:
        print('Youtube Downloader'.center(40, '_'))
        URL = input('Enter youtube url :  ')
        audio_downloader.extract_info(URL)
    except Exception:
        print("Couldn\'t download the audio")
    finally:
        option = int(input('\n1.download again \n2.Exit\n\nOption here :'))

        if option != 1:
            break
