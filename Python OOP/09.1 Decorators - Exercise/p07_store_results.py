class store_results:
    __log_file = "results.txt"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = (f"Function {self.function.__name__} was called. "
                  f"Result: {self.function(*args, **kwargs)}")
        with open(self.__log_file, "a") as file:
            file.write(f"{result}\n")
        return self.function(*args, **kwargs)
