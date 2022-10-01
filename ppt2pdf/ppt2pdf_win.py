# Note that comtypes is only available for Windows.
from comtypes.client import CreateObject, Constants


# Function PPTtoPDF
def PPTtoPDF(inputFileName, outputFileName, formatType=2):
    powerpoint = CreateObject('Powerpoint.Application')
    constants = Constants(powerpoint)
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, constants.PpSaveAsPDF)
    deck.Close()
    powerpoint.Quit()


# Function PPTtoPDFNote
def PPTtoPDFNote(inputFileName, outputFileName, formatType=32):
    powerpoint = CreateObject('Powerpoint.Application')
    constants = Constants(powerpoint)
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.ExportAsFixedFormat(
        outputFileName,
        constants.ppFixedFormatTypePDF,
        constants.ppFixedFormatIntentPrint,
        False,  # No frame
        constants.ppPrintHandoutHorizontalFirst,
        constants.ppPrintOutputNotesPages,
        constants.ppPrintAll
    )
    deck.Close()
    powerpoint.Quit()
