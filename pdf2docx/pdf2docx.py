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


def cloud_convert(app_sid, app_key):
    convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)     # Create instance of the API
    file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

    try:
        # upload source file to storage
        filename = input("Please enter the complete and correct file path of the required pdf: ")
        remote_name = filename
        output_name = remote_name.split('.')[0] + "docx"
        remote_name = filename
        strformat = 'docx'

        request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name, filename)
        file_api.upload_file(request_upload)

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


if __name__ == "__main__":

    choice = input("Press 1 for basic file conversion, 2 for advanced file conversion(GroupDocs account required)")
    while choice != '1' and choice != '2':
        print("Please enter a valid choice!\n")
        choice = input("Press 1 for basic file conversion, 2 for advanced file conversion(GroupDocs account required)")
    if choice == '1':

        pdf_path = input("Please enter the complete and correct file path of the required pdf: ")
        convert_pdf2docx(pdf_path)
    else:
        sid = input("Enter app SID: ")
        api_key = input("Enter api key: ")
        cloud_convert(sid, api_key)
