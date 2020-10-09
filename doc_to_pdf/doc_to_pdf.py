import comtypes.client
wdFormatPDF = 17


def doc_to_pdf(input_file_path, output_file_path):
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(input_file_path)
    doc.SaveAs(output_file_path, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
