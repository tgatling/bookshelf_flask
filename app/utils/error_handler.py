import logging


class ErrorHandler:
    @staticmethod
    def handle_error(error):
        logging.error(f"An error occurred: {str(error)}")
