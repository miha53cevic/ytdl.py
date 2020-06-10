
from setuptools import setup, find_packages

setup(
    name="ytdl.py",
    version="1.0",
    author="Mihael Petričević",
    packages=find_packages(),

    # Dependencies
    install_requires=["youtube_dl"],
    
    # Create a console script named music inside the python folder with scripts
    # that runs the main() function from music.py
    entry_points = {
        "console_scripts": ["ytdl=ytdl.ytdl:main"]
    },
);