import argparse
import random

def quicksort(array, n):
    if len(array) < 2 or n == 0:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less, n-1) + [pivot] + quicksort(greater, n-1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="number of elements to sort", type=int)
    args = parser.parse_args()
    array = [random.randint(0, 10) for i in range(args.n)]
    iterations = random.randint(1, 10)
    print(f'Unsorted array: {array}')
    print(f'what does this look like after {iterations} iterations of quicksort, where the pivot is the 0th element?')
    input('Press enter to for the answer...')
    print(quicksort(array , iterations))

if __name__ == "__main__":
    main()

