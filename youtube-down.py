"""
Disclaimer:
This script is provided for educational purposes only. The use of this script to download videos from YouTube may violate YouTube's terms of service or infringe on the rights of content creators. Please use this script responsibly and ensure that you have the necessary rights or permissions to download and use the videos.

By using this script, you agree that you are solely responsible for any legal consequences that may arise from your use of the script. The script author disclaims any liability or responsibility for the misuse or unauthorized use of this script.

Please review and comply with YouTube's terms of service and respect the rights of content creators.

Luka Beg 2023(c)
"""

from pytube import YouTube, Playlist

def select_video_format(video):
    print("Formats:")
    streams = video.streams.filter(file_extension='mp4').order_by('resolution').desc()
    for i, stream in enumerate(streams):
        print(f"{i + 1}. {stream.resolution} - {stream.mime_type}")

    print(f"{len(streams) + 1}. MP3")
    choice = int(input("Choice (number): "))
    return choice, streams

def download_video(url, format_choice, streams):
    yt = YouTube(url)
    if format_choice == len(streams) + 1:
        print(f"\nDownloading Audio: {yt.title}")
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(filename_prefix="audio_")
        print("Downloading audio completed!")
    else:
        stream = streams[format_choice - 1]
        print(f"\nDownloading Video: {yt.title} [{stream.resolution}]")
        stream.download()
        print("Downloading video completed!")

def download_playlist(url):
    playlist = Playlist(url)

    print(f"Playlist: {playlist.title}")
    print(f"Videos in playlist: {len(playlist)}")

    format_choice, streams = select_video_format(YouTube(playlist.video_urls[0]))

    for i, video_url in enumerate(playlist.video_urls):
        print(f"\nVideo to be downloaded: {i + 1} of {len(playlist)}")
        download_video(video_url, format_choice, streams)

    print("\nSuccessfully downloaded the playlist!")

def main():
    print("|---------------------|")
    print("|    youtube-down     |")
    print("|     by luka beg     |")
    print("|      (c) 2023       |")
    print("|---------------------|")
    print("")
    print("=======================")
    print("")
    url = input("URL: ")

    if "playlist" in url.lower():
        download_playlist(url)
    else:
        format_choice, streams = select_video_format(YouTube(url))
        download_video(url, format_choice, streams)

if __name__ == "__main__":
    main()
