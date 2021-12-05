from __future__ import unicode_literals
import yt_dlp

import argparse
import sys

def supported(url):
    ies = yt_dlp.extractor.gen_extractors()
    for ie in ies:
        if ie.suitable(url) and ie.IE_NAME != 'generic':
            # Site has dedicated extractor
            return True
    return False

def downloadFile(file: str):
    if (supported(file) == True):
        
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([file]);
    else:
        print(">>> Url invalid!");

def downloadPlaylist(playlist: str):
    if (supported(playlist) == True):
        
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'noplaylist': False,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist]);
    else:
        print(">>> Url invalid!");


def main():
    parser = argparse.ArgumentParser();
    parser.add_argument("url", help="youtube url");
    # action="store_true" means that when not specifying it, it returns false otherwise it returns true
    parser.add_argument("--playlist", "-p", help="download youtube playlist", action="store_true");

    if (len(sys.argv) > 1):
        args = parser.parse_args();
        if args.playlist == True:
            downloadPlaylist(args.url or "");
        else:
            downloadFile(args.url or "");
    else:
        print(">>> No url given!");
        

if __name__ == "__main__":
    main();