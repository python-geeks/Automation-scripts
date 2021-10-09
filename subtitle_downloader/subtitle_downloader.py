# Importing necessary modules
import sys
from youtube_transcript_api import YouTubeTranscriptApi

if len(sys.argv) != 2:
    print("Enter valid number of arguments")
    print("Try python subtitle_downloader.py <video link>")
    sys.exit()

# The list of dictionaries obtained by the the get_transcript() function
# is stored in sub variable
url = sys.argv[1].split("?v=")[1]
sub = YouTubeTranscriptApi.get_transcript(url)

# Writing subtitles into a file.
with open("subtitles.txt", "w") as f:
    for i in sub:
        f.write("{}\n".format(i))
