class Rule:

    def __init__(self, name, delimiter, responses):
        self.name = name
        self.delimiter = delimiter
        self.responses = responses


    def get_name(self):
        return self.name

    def get_delimiter(self):
        return self.delimiter

    def get_responses(self):
        return self.responses

    def set_name(self,name):
        self.name = name

    def set_delimiter(self, delimiter):
        self.delimiter = delimiter

    def set_responses(self, responses):
        self.responses = responses


class Response:

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message



class Variable:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value


class Learn:

    def __init__(self, var):
        self.var = var

    def get_var(self):
        return self.var

    def set_var(self, var):
        self.var = var


class Forget:

    def __init__(self, var):
        self.var = var

    def get_var(self):
        return self.var

    def set_var(self, var):
        self.var = var


class Action:

    def __init__(self, action, parameter):
        self.action = action
        self.parameter = parameter

    def get_action(self):
        return self.action

    def get_parameter(self):
        return self.parameter

    def set_action(self, action):
        self.action = action

    def set_parameter(self, parameter):
        self.parameter = parameter
