import os
import pandas as pd
from django.core.exceptions import ValidationError


class FileManager:
    def __init__(self):
        pass

    def check_file_type(self, file) -> str:
        """Check the extension of the file"""
        extension = os.path.splitext(file.name)[1]
        return extension

    def read_file_by_file_extension(self, file) -> str:
        """Read the content of the file if it's .xlsx or .csv"""
        file_type = self.check_file_type(file)

        if file_type == '.xlsx':
            read_file = pd.read_excel(file)
            return read_file
        elif file_type == '.csv':
            read_file = pd.read_csv(file)
            return read_file
        else:
            return None
