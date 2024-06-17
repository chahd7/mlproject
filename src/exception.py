import sys # Provides information about exceptions
from src.logger import logging 

def error_message_detail(error, error_detail: sys): # Function to create a detailed error message when an exception is raised
    _, _, exc_tb = error_detail.exc_info() # Extract the traceback object which contains information about the exception
    file_name = exc_tb.tb_frame.f_code.co_filename # Get the file name where the exception occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message : [{2}]".format( # Format the error message
        file_name, exc_tb.tb_lineno, str(error) # Insert the file name, line number, and error message into the formatted string
    )

    return error_message # Return the formatted error message

class CustomException(Exception): # Define a custom exception class inheriting from the base Exception class
    def __init__(self, error_message, error_detail: sys): # Initialization method for the custom exception
        super().__init__(error_message) # Call the base class constructor with the error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail) # Generate detailed error message and store it in the instance

    def __str__(self): # Define the string representation of the custom exception
        return self.error_message # Return the detailed error message when the exception is printed or converted to a string
