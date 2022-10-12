
def list_to_int_decorator(func):
    '''
    Function to convert function result to string
    '''
    def wrapper(*args, **kwargs):

        res = func(*args, **kwargs)
        listToStr = ' '.join([str(elem) for elem in my_list])
        print('Result converted to string: ' + listToStr)
        return res

    return wrapper


@list_to_int_decorator
def my_function1(lst1):

    lst1.append(1)

    return lst1

my_list = [1, 2, 3]
my_list = my_function1(my_list)









