import urllib.request
import re

# Prepare the link with query
search = input("Search For: ")
search = search.replace(" ", "+")
url = f"https://www.youtube.com/results?search_query=${search}"

html = urllib.request.urlopen(url)

# Each video has a unique identifier so we need to fetch them all
# Reg exp to find all identifiers in our page
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

# Generate Links
videos_link = []
for i in range(len(video_ids)):
    videos_link.append(f"https://www.youtube.com/watch?v={video_ids[i]}")
for video in videos_link:
    print(video)
