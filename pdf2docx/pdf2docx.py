# Import Libraries
from pdf2docx import parse
from typing import Tuple
import groupdocs_conversion_cloud


def convert_pdf2docx(input_file: str, pages: Tuple = None):

    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file, pages=pages)
    print("###### Conversion Complete #######")
    return result

def cloud_convert (app_sid,app_key):
    convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)     # Create instance of the API
    file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

    try:

        filename = input("Please enter the complete and correct file path of the required pdf: ")    # upload source file to storage
        remote_name = filename
        output_name = remote_name.split('.')[0] + "docx"
        remote_name = filename
        strformat = 'docx'

        request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name, filename)

        response_upload = file_api.upload_file(request_upload)

        # Extract Text from PDF document

        settings = groupdocs_conversion_cloud.ConvertSettings()

        settings.file_path = remote_name

        settings.format = strformat

        settings.output_path = output_name

        request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)

        response = convert_api.convert_document(request)

        print("Document converted successfully: " + str(response))

    except groupdocs_conversion_cloud.ApiException as e:
        print("Exception when calling get_supported_conversion_types: {0}".format(e.message))

    return


if __name__ == "__main__":


    choice= input("For basic file conversion press 1, for advanced conversion press 2 (GroupDocs Conversion SDK and API required): ")
    while choice != '1' and choice != '2':
        print("Please enter a valid choice!\n")
        choice = input("For basic file conversion press 1, for advanced conversion press 2 (GroupDocs Conversion SDK and API required): ")
    if choice == '1':

        input_file = input("Please enter the complete and correct file path of the required pdf: ")
        convert_pdf2docx(input_file)
    else:
        app_sid = input("Enter app SID: ")
        app_key = input("Enter api key: ")
        cloud_convert(app_sid,app_key)

