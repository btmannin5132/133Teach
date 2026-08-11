from vector_operations import add_vectors as av

def main_function():
    X = [1, 2]
    Y = [3, 4]
    Z = av(X, Y)
    print(f"Adding {X} and {Y} is {Z}")


if __name__ == "__main__":
    main_function()