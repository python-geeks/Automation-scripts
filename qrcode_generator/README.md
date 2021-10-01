# QR Code Generator
### Desktop App to convert anything to QR Code!

#### Currently supports the following file types
- Portable Document Format (PDF)
- Microsoft Word
- Microsoft Powerpoint
- Images (JPEG, PNG)
- Text/URL

Text/URL are processed locally.
Other file types require access to Google Drive where the files are uploaded.<br><br>

## How to Run
- Create a [Python Virtual Environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (Recommended)
- Download the following python modules
  - qrcode
  - tkinter
  - Google Client Library

- Run the code:
<pre><code>python3 qr_generator.py</code></pre>

<br><br>

## Behind the Scenes
- Text and URL are processed locally using qrcode module in python
- Other media types including pdf, images, ms word, ppt need to be visible universally so that anyone can access the file. This is done by publishing files on the cloud using the Google Drive API. 
- This will request the user account authentication to access drive done using Google's secure OAuth 2.0
- Python code uploads file, modifies visibility permissions and retrieves shareable URL
