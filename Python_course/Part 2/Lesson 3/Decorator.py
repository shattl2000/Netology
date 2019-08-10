from datetime import datetime


def decorate(path):
    def decorator_logger(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            name_func = func.__name__
            func(*args)
            with open(path, 'w', encoding='utf8') as file:
                to_write = f'{start_time} {name_func} {args} {func(*args, **kwargs)}'
                file.write(str(to_write))
        return wrapper
    return decorator_logger


@decorate('log.txt')
def amount(a, b):
    result = a + b
    return result


if __name__ == '__main__':
    amount(3, 7)
