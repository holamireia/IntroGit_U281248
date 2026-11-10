# Mi primer archivo rastreado por Git
# Autor: Mireia Delgado Estudillo
def greet(name):
    """Devuelve un mensaje dado para el nombre dado."""
    return f"Hello, {name}! Welcome to Git."
def farewell(name):
    """Devuelve un mensaje de despedida para el nombre dado."""
    return f"Goodbye, {name}! See you next commit."
if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))