def collatz_iter(n):
    #Determine stopping time using iteration.
    steps = 0
    while n > 1:
        steps += 1
        if n%2:  # n is odd​
            n = 3*n + 1
        else:  # n is even​
            n = n // 2
    return steps

def collatz_recur(n, steps):
#    Determine stopping time using recursion.
    if n == 1:
        return steps
    elif n%2:  # n is odd​
        n = 3*n + 1
    else:  # n is even​
        n = n //  2
    return collatz_recur(n, steps+1)

def hanoiRecurs(n, source, auxiliary, destination):
    """
    Solves the Towers of Hanoi puzzle recursively.
        n: The number of disks to move.
        source: The starting peg.
        auxiliary: The intermediate peg.
        destination: The final peg.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoiRecurs(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoiRecurs(n - 1, auxiliary, source, destination)


if __name__ == "__main__": # if this is the file being executed (instead of being imported):
    #collatz_iter(123)
    #collatz_recur(123,0)
    hanoiRecurs(5, 'A', 'B', 'C')