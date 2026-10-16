import time

LAST_NAME = "Gabilan"
STUDENT_ID = "TUPM-26-2636"
FAVORITE_ARTIST = "The 1975"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)

ARTIST_SUM = sum(
    ord(char.upper()) - ord('A') + 1
    for char in FAVORITE_ARTIST
    if char.isalpha()
)


def bubble_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(a)):
        swapped = False

        for j in range(len(a) - i - 1):
            comparisons += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                movements += 1
                swapped = True

        if not swapped:
            break

    return a, comparisons, movements


def selection_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(a) - 1):
        minimum = i

        for j in range(i + 1, len(a)):
            comparisons += 1

            if a[j] < a[minimum]:
                minimum = j

        if minimum != i:
            a[i], a[minimum] = a[minimum], a[i]
            movements += 1

    return a, comparisons, movements


def insertion_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] <= key:
                break

            a[j + 1] = a[j]
            movements += 1
            j -= 1

        a[j + 1] = key

    return a, comparisons, movements


orders = [
    (ID_SUM * 3 + i * 7 + SEED_DIGIT + ARTIST_SUM) % 1000
    for i in range(20)
]

inputs = {
    "Sorted": sorted(orders),
    "Reverse": sorted(orders, reverse=True),
    "Random": orders.copy()
}

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

print("Generated Order Dataset:", orders)

for condition, dataset in inputs.items():
    print(f"\n{condition} Input:", dataset)

    for name, algorithm in algorithms.items():
        start = time.perf_counter()
        result, comparisons, movements = algorithm(dataset)
        elapsed = time.perf_counter() - start

        print(
            f"{name}: Comparisons={comparisons}, "
            f"Movements={movements}, "
            f"Time={elapsed:.8f} s, "
            f"Sorted Correctly={result == sorted(dataset)}"
        )

print("\nBig O Analysis:")
print("Bubble Sort: O(n^2) average and worst case")
print("Selection Sort: O(n^2) average and worst case")
print("Insertion Sort: O(n^2) average and worst case")
print("Insertion Sort: O(n) best case")
print("Optimized Bubble Sort: O(n) best case")