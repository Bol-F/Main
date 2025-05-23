import logging

logging.basicConfig(filename='file_for_Norm8.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_decor(func):
    def inner(*args, **kwargs):
        logging.info(f'Calling {func.__name__}')
        try:
            ans = func(*args, **kwargs)
            logging.info(f'{func.__name__} is returned: {ans}')
            return ans
        except Exception as e:
            logging.error(f'{func.__name__} raised an exception: {e}')

    return inner


@log_decor
def add_nums(*args, **kwargs):
    s = list(args) + list(kwargs.values())
    return sum(s)


@log_decor
def mul_nums(*args, **kwargs):
    m = 1
    for i in args:
        m *= i
    for i in kwargs.values():
        m *= i
    return m


@log_decor
def greatest_num(*args, **kwargs):
    s = list(args) + list(kwargs.values())
    return max(s)


mul_nums(1, 5, 8)
add_nums(1, 5, 8)
greatest_num(1, 5, 8)


def count_to_n(n):
    for i in range(1, n + 1):
        yield i


print(list(count_to_n(4)))
