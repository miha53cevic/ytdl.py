
from setuptools import setup, find_packages

setup(
    name="ytdl.py",
    version="1.1",
    author="miha53cevic",
    packages=find_packages(),

    # Dependencies
    install_requires=["yt-dlp"],
    
    # Create a console script named ytdl inside the python folder with scripts
    # that runs the main() function from ytdl.py
    entry_points = {
        "console_scripts": ["ytdl=ytdl.ytdl:main"]
    },
);