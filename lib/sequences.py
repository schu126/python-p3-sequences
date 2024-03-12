#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0, 1]
    if length <= 0:
        sequence = []
    elif length == 1:
        sequence = [0]
    elif length > 2:
        for i in range(2, length):
            sequence.append(sequence[i-1] + sequence[i-2])
    print(sequence)

