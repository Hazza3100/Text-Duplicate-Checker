import Levenshtein


def check_duplicates(text_list, threshold=0.8):
    duplicates = []
    n = len(text_list)

    for i in range(n):
        for j in range(i + 1, n):
            similarity = 1 - Levenshtein.distance(text_list[i], text_list[j]) / max(len(text_list[i]), len(text_list[j]))
            if similarity >= threshold:
                duplicates.append((text_list[i], text_list[j], similarity))

    return duplicates


# Example usage
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "The quick brown fox jumps over the lazy dog",
    "The quick brown fox jumps over the lazy cat.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing.",
    "Suspendisse potenti. Nullam efficitur posuere justo vitae.",
]

duplicate_threshold = 0.8
result = check_duplicates(texts, duplicate_threshold)

if len(result) > 0:
    print("Duplicates found:")
    for duplicate in result:
        text1, text2, similarity = duplicate
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")
        print(f"Similarity: {similarity}")
        print()
else:
    print("No duplicates found.")
