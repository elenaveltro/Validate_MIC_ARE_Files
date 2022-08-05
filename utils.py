from Exceptions.CustomExceptions import ExcelException


def check_valid_list(sheet, df, column, row):
    if df[column][row].count('[') != df[column][row].count(']'):
        error_message = "ERROR! Malformed list. Sheet '{}', Key '{}', Column '{}' (Row {}) ".format(sheet,
                                                                                                    df['KEY'][row],
                                                                                                    column, row + 2)
        raise ExcelException(msg=error_message)


def check_number_element(first_df, second_df, first_col, second_col, row):
    first_str = first_df[first_col][row].replace(" ", "")
    first_strs = first_str.replace('[', '').split('],')
    first_list = [s.replace(']', '').split(',') for s in first_strs]

    second_str = second_df[second_col][row].replace(" ", "")
    second_strs = second_str.replace('[', '').split('],')
    second_list = [s.replace(']', '').split(',') for s in second_strs]

    if len(first_list) != len(second_list):
        error_message = "ERROR! The number of elements does not match between columns '{}' - '{}'." \
                        " Key '{}' (Row {})".format(first_col, second_col, first_df['KEY'][row], row + 2)
        raise ExcelException(msg=error_message)

    for index, elem in enumerate(first_list):
        if isinstance(elem, list) and len(elem) != len(second_list[index]):
            if len(elem) < len(second_list[index]):
                error_message = "ERROR! The number of elements of element {} does not match between " \
                                "columns: '{}' - '{}'. Key '{}' (Row {})".format(index, first_col, second_col,
                                                                                 first_df['KEY'][row],
                                                                                 row + 2)
            raise ExcelException(msg=error_message)
