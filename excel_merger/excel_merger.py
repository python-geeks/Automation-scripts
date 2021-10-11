"""
Merges two excels into one copying all the sheets.
"""
import os

import openpyxl
import pandas as pd


def get_all_sheet_names(url_, url2_):
    """
    Get the two xlsx files sheet names from their url
    """
    xls = pd.read_excel(url_, sheet_name=None)
    xls2 = pd.read_excel(url2_, sheet_name=None)
    return xls.keys(), xls2.keys()


def check_if_file_exists(destination_file):
    """
    if a file does not exist, create an xlsx file where merged data is stored.
    """
    if not os.path.exists(destination_file):

        wb_ = openpyxl.Workbook()
        wb_.save(destination_file)


def write_to_excel(sheet_one_names, sheet_two_names, url, url2, destfile):
    """
    Write to destination excel
    """

    for i in sheet_one_names:
        data = pd.read_excel(url, sheet_name=i)
        with pd.ExcelWriter(destfile, engine="openpyxl", mode="a") as writer:
            data.to_excel(writer, index=False, sheet_name=i)

    for i in sheet_two_names:
        data = pd.read_excel(url2, sheet_name=i)
        with pd.ExcelWriter(destfile, engine="openpyxl", mode="a") as writer:
            data.to_excel(writer, index=False, sheet_name=i)

    # remove the extra Sheet added if exists while creating the destfile
    if "Sheet" not in sheet_one_names and "Sheet" not in sheet_two_names:
        workbook1 = openpyxl.load_workbook(destfile)
        del workbook1["Sheet"]
        workbook1.save(destfile)


def run_the_flow(url, url2, destfile):
    """
    Run the flow for the merging of two excels into one.
    """
    sheet_one_names, sheet_two_names = get_all_sheet_names(url, url2)
    check_if_file_exists(destfile)
    write_to_excel(sheet_one_names, sheet_two_names, url, url2, destfile)


if __name__ == "__main__":

    URL1 = r"C:\Users\ShashwatKumar\Desktop\open_source\
    Automation-scripts\excel_merger\files\FoodSales1-1.xlsx"
    URL2 = r"C:\Users\ShashwatKumar\Desktop\open_source\
    Automation-scripts\excel_merger\files\FoodSales2-1.xlsx"
    DEST = r"C:\Users\ShashwatKumar\Desktop\open_source\
    Automation-scripts\excel_merger\merged\merged.xlsx"

    run_the_flow(URL1, URL2, DEST)
