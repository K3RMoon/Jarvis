class Rule:

    def __init__(self, name, delimiter, responses):
        self.name = name
        self.delimiter = delimiter
        self.responses = responses


    def get_name(self):
        return self.name

    def get_delimeter(self):
        return self.delimiter

    def get_delimeter(self):
        return self.responses


class Response:

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message



class Variable:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

