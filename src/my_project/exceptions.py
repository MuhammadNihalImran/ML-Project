import sys
from src.my_project.logger import logging


def error_message_details(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line: {line_number} with message: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(
            error_message,
        )
        self.message = error_message_details(error_message, error_details)

    def __str__(self):
        return self.message
