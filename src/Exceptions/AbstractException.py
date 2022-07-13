class AbstractException(Exception):
    def __init__(self, message):
        super().__init__("Error: " + message + "!")
