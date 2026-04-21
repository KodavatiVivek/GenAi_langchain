import sys
from pathlib import Path


def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Builds a detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return f"Error occurred: {str(error)}"

    file_name = Path(exc_tb.tb_frame.f_code.co_filename).name
    line_number = exc_tb.tb_lineno

    return f"Error in [{file_name}] at line [{line_number}] : {str(error)}"


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message