"""
@ Description
    Non functional example of error handling

    Quick list of error provided by Python API
        IndexError
        OSError
        ValueError
        RuntimeError
        TypeError
        NameError

@ Pass/Fail @b criteria
    None

@ Usage
    From terminal:
        error_handling_example.py
"""


class MessyClassError(Exception):
    def __init__(self, message):
        super(exampleError, self).__init(message)


class MessyClass:
    def __init__(self):
        print("Object built successfully ")

    def example_try_except_text(self):
        try:
            operation_that_can_throw_ioerror()
        except ErrorToBeCatched:
            handle_the_exception_somehow

    def example_try_except_else_finally(self):
        try:
            operation_that_can_throw_error()
        except ErrorToBeCatched():
            handle_the_exception_somehow()
        else:
            another_operation_that_can_throw_error()
        finally:
            something_we_always_need_to_do()

    def example_of_raise_1(self):
        if wrong_condition:
           raise #Empty should return original error

    def example_of_raise_2(self):
        if wrong_condition:
           raise ValueError ("Error message here")

    def example_of_error_mask:
        try:
            operation_that_can_throw_ioerror()
        except ErrorToBeCatched as ErrorObject:
            message = "error bla bla"
            return message + ErrorObject


if __name__ == "__main__":
    #This function do nothing, it
    print("Non functional example")
