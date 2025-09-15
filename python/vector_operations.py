def add_vectors(A, B):
    return [A[0] + B[0], A[1] + B[1]]

if __name__ == "__main__":
    
    result = add_vectors([1, 2], [3, 4])

    print(result)