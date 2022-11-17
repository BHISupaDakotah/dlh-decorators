import functools
import copy

def convert_to_strings(func):
  @functools.wraps(func)
  def wrapper_func(*args, **kwargs):
    item_list = args[0] # args[0] is a reference to a list in memory
                        # item_list is also a reference to the same list in the same postition in memory
    for i in range(len(item_list)):
      item_list[i] = str(item_list[i])
    
    return(
      func( *args, **kwargs)
    )

  return wrapper_func

def convert_to_numbers(func):
  @functools.wraps(func)
  def wrapper_func(*args, **kwargs):
    item_list = args[0]

    for i in range(len(item_list)):
      item_list[i] = int(item_list[i])
    
    return(
      func( *args, **kwargs)
    )

  return wrapper_func


def pass_by_value(func):
  @functools.wraps(func)
  def wrapper_func(*args, **kwargs):

    new_args = copy.deepcopy(args)
    new_kwargs = copy.deepcopy(kwargs)

    
    return(
      func( *new_args, **new_kwargs)
    )

  return wrapper_func

  