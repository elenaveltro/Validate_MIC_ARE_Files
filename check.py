import pandas as pd
import sys

from Exceptions.CustomExceptions import GenericException, ExcelException
from utils import check_valid_list, check_number_element

sheet1 = 'KPIs'
sheet2 = 'THRESHOLDS'

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise GenericException(msg="Missing file name! \n \nEx. pyhton check.py <nome_file>")

    filename = sys.argv[1] if (sys.argv[1].endswith(".xlsx") or sys.argv[1].endswith(".xls")) else sys.argv[1] + ".xlsx"
    print("Starting validate file {} . . .".format(filename))

    xls = pd.ExcelFile(filename)
    df1 = pd.read_excel(xls, sheet1)
    df2 = pd.read_excel(xls, sheet2)

    if len(df1) != len(df2):
        error_message = "ERROR: Sheets {} and {} do not have the same number of rows".format(sheet1, sheet2)
        raise ExcelException(msg=error_message)

    for i in range(len(df1)):
        # Check if there are missing brackets
        check_valid_list(sheet1, df1, 'KPI', i)
        check_valid_list(sheet1, df1, 'GAP UNDERPERFORMANCE INDICATOR', i)
        check_valid_list(sheet2, df2, 'GAP_THRESHOLD', i)

        # Check if the number of element is the same
        check_number_element(df1, df1, 'KPI', 'GAP UNDERPERFORMANCE INDICATOR', i)
        check_number_element(df1, df2, 'KPI', 'GAP_THRESHOLD', i)

    print("Everything is ok!")
