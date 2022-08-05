class GenericException(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)


class ExcelException(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)