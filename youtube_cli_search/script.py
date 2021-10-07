import urllib.request
import re

# Prepare the request link
search = input("Search For: ")
search = search.replace(" ", "+")
url = f"https://www.youtube.com/results?search_query={search}"
print(url)

# Getting html page
html = urllib.request.urlopen(url)

"""
Each video has a unique identifier so we need to fetch them all.
We can find all of those unique identifiers using regular expression.
"""
videos_identifiers = re.findall(r"watch\?v=(\S{11})", html.read().decode())

# Generate Links
videos_link = []
standard_video_link = "https://www.youtube.com/watch?v="
for i in range(len(videos_identifiers)):
    videos_link.append(f"{standard_video_link}{videos_identifiers[i]}")


print(f"status: Success,\n"
      f"result: {len(videos_link)},\n"
      f"links:")
for video in videos_link:
    print(video)
