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


def merge_sorted(a, b):
    i = 0
    j = 0
    merged = []
    comparisons = 0

    while i < len(a) and j < len(b):
        comparisons += 1

        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged, comparisons


department_a = sorted(
    SEED_DIGIT + ID_SUM + i * 3
    for i in range(10)
)

department_b = sorted(
    ARTIST_LENGTH + NAME_LENGTH + i * 4
    for i in range(10)
)

consolidated, comparisons = merge_sorted(department_a, department_b)

print("Department A Dataset:", department_a)
print("Department B Dataset:", department_b)
print("Consolidated Dataset:", consolidated)
print("Records Before Consolidation:", len(department_a) + len(department_b))
print("Records After Consolidation:", len(consolidated))
print("Comparison Count:", comparisons)
print("Ordering Verified:", consolidated == sorted(department_a + department_b))
print("Time Complexity: O(n + m)")
print("Space Complexity: O(n + m)")