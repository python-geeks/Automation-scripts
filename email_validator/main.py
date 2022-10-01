import config
# The quickemailverification module allows
# us to verify email addresses in bulk.
import quickemailverification
# The openpyxl module allows your Python programs
# to read and modify Excel spreadsheet files.
import openpyxl
from openpyxl.styles import Font


# Function to write the labels for the columns in the Excel spreadsheet
def write_header_row():
    sheet = wb.active
    # Change the sheet name of the workbook
    sheet.title = "Email Validator"
    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['C'].width = 20
    sheet.column_dimensions['D'].width = 17
    sheet.column_dimensions['E'].width = 17
    sheet.column_dimensions['H'].width = 25
    sheet.column_dimensions['I'].width = 14
    sheet.column_dimensions['J'].width = 40
    sheet.column_dimensions['K'].width = 20
    sheet.column_dimensions['L'].width = 20
    sheet.column_dimensions['M'].width = 30
    sheet.column_dimensions['N'].width = 10
    sheet.column_dimensions['O'].width = 20
    header_row_font = Font(size=14, bold=True)
    labels = {
        'A': "Email",
        'B': "Result",
        'C': "Reason",
        'D': "Disposable",
        'E': "Accept All",
        'F': "Role",
        'G': "Free",
        'H': "User",
        'I': "Domain",
        'J': "MX Record",
        'K': "MX Domain",
        'L': "Safe to Send",
        'M': "Did You Mean?",
        'N': "Success",
        'O': "Message"}

    for column in labels:
        label = labels[column]
        sheet[f'{column}1'].font = header_row_font
        sheet[f'{column}1'] = label
    wb.save('result.xlsx')


def add_data_in_column(response):
    sheet = wb.active
    data_font = Font(size=12)

    columns = {
        "email": 'A',
        "result": 'B',
        "reason": 'C',
        "disposable": 'D',
        "accept_all": 'E',
        "role": 'F',
        "free": 'G',
        "user": 'H',
        "domain": 'I',
        "mx_record": 'J',
        "mx_domain": 'K',
        "safe_to_send": "L",
        "did_you_mean": "M",
        "success": 'N',
        "message": 'O'}

    # Each time this function is called, the result
    # corresponding to that email would be printed on a new row.
    max_filled_row = sheet.max_row + 1
    for label in response:
        data = response[label]
        # Using columns dictionary, determine the column
        # number in which the data should be displayed.
        column = columns[label]
        sheet[f"{column}{max_filled_row}"].font = data_font
        sheet[f"{column}{max_filled_row}"] = data
    wb.save('result.xlsx')


if __name__ == "__main__":
    # Start a connection to QuickEmailVerification
    client = quickemailverification.Client(config.api_key)
    quickemailverification = client.quickemailverification()

    # Create an Excel Workbook.
    wb = openpyxl.Workbook()

    # Read the emails from the txt file and verify it.
    with open(r"email_list.txt") as f:
        emails = f.read().split("\n")
        for email in emails:
            response = quickemailverification.verify(email)
            if response.body['success'] == 'false':
                print("API Key is invalid. Follow the instructions ", end="")
                print("in README.md to get an API key.")
                break
            else:
                add_data_in_column(response.body)
        else:
            # The Excel file should be created only if the API Key is valid.
            write_header_row()
