films = ['Spider-man',
 'Die Hard',
 'Batman and Robin',
 'Home Alone',
 'Seven',
 "Harry Potter"]


def decorator_func(func):
  def wrapper():
    print('I am in decorator')
    func_result = func()
    if func_result:
      films.pop()
      print(films.pop())
  return wrapper


@decorator_func
def hello_world():
  if len(films) > 5:
    return True
  else:
    return False


hello_world()