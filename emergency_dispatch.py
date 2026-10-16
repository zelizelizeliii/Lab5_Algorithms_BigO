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

LAST_NAME = "Gabilan"
STUDENT_ID = "TUPM-26-12345"
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


def linear_search(data, target):
    comparisons = 0

    for i, value in enumerate(data):
        comparisons += 1
        if value == target:
            return i, comparisons

    return -1, comparisons


def rotated_search(data, target):
    low, high = 0, len(data) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if data[mid] == target:
            return mid, comparisons

        if data[low] <= data[mid]:
            if data[low] <= target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if data[mid] < target <= data[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1, comparisons


original = sorted(set(
    (ID_SUM + i * 7 + ARTIST_SUM) % 1000
    for i in range(20)
))

rotation_point = SEED_DIGIT % len(original)

rotated = (
    original[rotation_point:]
    + original[:rotation_point]
)

target = original[(ID_SUM + ARTIST_SUM) % len(original)]

rotated_index, rotated_comparisons = rotated_search(rotated, target)
linear_index, linear_comparisons = linear_search(rotated, target)

print("Original Dataset:", original)
print("Rotated Dataset:", rotated)
print("Target Incident:", target)
print("Rotated Search Position:", rotated_index)
print("Rotated Search Comparisons:", rotated_comparisons)
print("Linear Search Position:", linear_index)
print("Linear Search Comparisons:", linear_comparisons)
print("Time Complexity: O(log n) average for this search method")
print("Space Complexity: O(1)")