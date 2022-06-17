def take_first(todos):
    # Improve this so that it doesn't explode if given an empty list.
    """
    Accepts a list of todos and removes the first.

    Args:
        todos: A list of dicts.

    Returns:
        todo: A dict popped off the list
        todos: A tuple of the remaining todos

        OR

        None
        todos: An empty tuple

    >>> todos = [{'name': 'Example 1', 'body': 'Test task', 'points': '1'},
    ... {'name': 'Example 2', 'body': 'Second task', 'points': '2'}]
    >>> todo, todos = take_first(todos)
    >>> todo
    {'name': 'Example 1', 'body': 'Test task', 'points': '1'}
    >>> todos
    [{'name': 'Example 2', 'body': 'Second task', 'points': '2'}]
    >>> todos = []
    >>> take_first(todos)
    (None, [])
    """

    # Right I need to treat doctests like a repl lol
    if todos:
        todo = todos.pop(0)
        return (todo, todos)
    else:
        return (None, todos)

def sum_points(todos):
    # Modify this so that it can sum more than two values.
    """
    Args:
        todos: A list of dictionaries with 'point' key value pairs, sums their point values.

    Returns:
        integer: The sum of the point values of each todo in todos

    >>> todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '1'},
    ... {'name': 'Example 2', 'body': 'Second task', 'points': '2'},
    ... {'name': 'Example 3', 'body': 'Third task', 'points': '3'}]
    >>> sum_points(todos)
    6
    """
    total = 0
    for todo in todos:
        total += int(todo['points'])
    return total
