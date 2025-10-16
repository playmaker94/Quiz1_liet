def compare_strings(s1, s2, verbose=True):
    matches = 0
    total = len(s1)
    report_line = ""

    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            matches += 1
            report_line += "✔ "
        else:
            report_line += "✘ "

    similarity = (matches / total) * 100

    if verbose:
        print("\n🔍 Match Report:")
        print("String 1: ", s1)
        print("String 2: ", s2)
        print("Match   : ", report_line)
        print(f"\n✅ Similarity: {similarity:.2f}%")

    return similarity, matches, total


def calculate_similarity(s1, s2):
    len1, len2 = len(s1), len(s2)

    if len1 != len2:
        max_similarity = 0
        best_s1 = s1
        best_s2 = s2

        if len1 < len2:
            pad = len2 - len1
            for i in range(pad + 1):
                aligned = " " * i + s1 + " " * (pad - i)
                score = compare_strings(aligned, s2, verbose=False)[0]
                if score > max_similarity:
                    max_similarity = score
                    best_s1 = aligned
                    best_s2 = s2
        else:
            pad = len1 - len2
            for i in range(pad + 1):
                aligned = " " * i + s2 + " " * (pad - i)
                score = compare_strings(s1, aligned, verbose=False)[0]
                if score > max_similarity:
                    max_similarity = score
                    best_s1 = s1
                    best_s2 = aligned

        return compare_strings(best_s1, best_s2)
    else:
        return compare_strings(s1, s2)
