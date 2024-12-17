class IncorrectCRSException(Exception):
    def __init__(self, crs_value: str):
        self.message = f"The value {crs_value} is invalid to map CRS"
        super().__init__(self.message)
