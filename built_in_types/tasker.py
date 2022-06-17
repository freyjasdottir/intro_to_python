def print_todo(todo):
  """
  Accepts a dictionary (todo) and prints it, delimiting with a colon (:)

  Args:
      todo (dict): A dictionary with keys 'name' 'body' and
      'points', all strings.

  Returns:
      null. Prints the name and body values in todo.

  Raises:
      n/a

  >>> todo = {'name': 'Example 1', 'body': 'This is a test task', 'points': '3'}
  >>> print_todo(todo)
  Example 1: This is a test task
  >>>
  """
  print(f"{todo[ 'name' ]}: {todo[ 'body' ]}")

def take_first(todos):
    """
    Accepts a list of todos and removes the first.

    Args:
        todos: A list of dicts.

    Returns:
        todo: A dict popped off the list
        todos: A tuple of the remaining todos

    >>> todos = [{'name': 'Example 1', 'body': 'Test task', 'points': '1'},
    ... {'name': 'Example 2', 'body': 'Second task', 'points': '2'}]
    >>> todo, todos = take_first(todos)
    >>> todo
    {'name': 'Example 1', 'body': 'Test task', 'points': '1'}
    >>> todos
    [{'name': 'Example 2', 'body': 'Second task', 'points': '2'}]
    """

    # Right I need to treat doctests like a repl lol
    todo = todos.pop(0)
    return (todo, todos)

def sum_points(todo1, todo2):
    """
    Args:
        todo1, todo2: Dictionaries with 'point' key value pairs, sums their point values.

    Returns:
        integer: The sum of the point values of todo1 and todo2

    >>> todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '1'},
    ... {'name': 'Example 2', 'body': 'Second task', 'points': '2'}]
    >>> sum_points(todos[0], todos[1])
    3
    """
    return int(todo1['points']) + int(todo2['points'])
