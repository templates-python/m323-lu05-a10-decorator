def count_calls(original_function):
    """
    Ein Decorator, der die Anzahl der Aufrufe einer Funktion zählt.

    Args:
        original_function (function): Die Funktion, deren Aufrufe gezählt werden sollen.

    Returns:
        function: Eine dekorierte Version der ursprünglichen Funktion, die die Anzahl der Aufrufe zählt.
    """
    ...

@count_calls
def my_function():
    print("Ich tue etwas")

#Testen Sie Ihren Decorator
if __name__ == '__main__':
    my_function()
    my_function()