def iterable(cls):
    """ Décorateur pour rendre une classe iterable. """

    def iter_fn(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    cls.__iter__ = iter_fn
    return cls


def timer(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took {time.time() - start:.02f} seconds')

        return result

    return wrapper


def logger(func):
    import logging

    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='example.log', level=logging.INFO)
        logging.info(f'Running {func.__name__} with args: {args} and kwargs: {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Finished {func.__name__}')
        return result

    return wrapper
