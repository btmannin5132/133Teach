import vector_operations

def main_function():
    X = [1, 2]
    Y = [3, 4]
    Z = vector_operations.add_vectors(X, Y)
    print(f"Adding {X} and {Y} is {Z}")


if __name__ == "__main__":

    main_function()