from __future__ import unicode_literals
import youtube_dl

import argparse
import sys

def supported(url):
    ies = youtube_dl.extractor.gen_extractors()
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
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([file]);
    else:
        print(">>> Url invalid!");


def main():
    parser = argparse.ArgumentParser();
    parser.add_argument("url", help="youtube url");

    if (len(sys.argv) > 1):
        args = parser.parse_args();
        downloadFile(args.url or "");
    else:
        print(">>> No url given!");
        

if __name__ == "__main__":
    main();