#!/usr/bin/env python
import pdfkit
import sys


class MediumToPdf():
    """
    This class contains method to convert a medium article into pdf file.
    """
    def __init__(self, url, output_file):
        """
        url: The url of medium article.
        output_file: The name of the output file.
        """
        self.convert_to_pdf(url, output_file)

    def convert_to_pdf(self, url, output_file):
        """
        url: The url of medium article.
        output_file: The name of the output file.
        """
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
        }
        pdfkit.from_url(url, output_file, options=options)


if __name__ == "__main__":
    url = sys.argv[sys.argv.index('--url') + 1]
    output_file = sys.argv[sys.argv.index('--output') + 1]
    try:
        medium_to_pdf = MediumToPdf(url, output_file)
    except Exception as e:
        print("An error arised. ", e)
