import random
import argparse

def mergesort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        left = mergesort(array[:mid])
        right= mergesort(array[mid:])
        print(f'left: {left}')
        print(f'right: {right}')
        print('merging...')
        merged = merge(left, right)
        print(f'merged: {merged}')
        return merged
    
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="number of elements in the array", type=int)
    args = parser.parse_args()
    lst = [random.randint(0, 10) for i in range(args.n)]

    print(f'Unsorted array: {lst}')
    print(f'How many merges were performed after a merge sort of this array?')
    input('Press enter to for the answer...')
    print(mergesort(lst))

if __name__ == "__main__":
    main()
