from vector_operations import add_vectors

def main_function():
    X = [1, 2]
    Y = [3, 4]
    Z = add_vectors(X, Y)
    print(f"Adding {X} and {Y} is {Z}")


if __name__ == "__main__":
    main_function()