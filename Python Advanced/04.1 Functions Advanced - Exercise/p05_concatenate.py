def concatenate(*args, **kwargs):
    concatenated_args = "".join(args)

    for (given_key, argument) in kwargs.items():
        if given_key in concatenated_args:
            concatenated_args = concatenated_args.replace(given_key, argument)
    return concatenated_args
