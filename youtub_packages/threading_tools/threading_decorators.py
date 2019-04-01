import threading


def threaded_fn(func):
    """
    A decorator for any function that needs to be run on a separate thread
    """
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper
