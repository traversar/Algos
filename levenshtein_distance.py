def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small)) + 1]
    oddEdits = [None for x in range(len(small)) + 1]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            curr = oddEdits
            prev = evenEdits
        else:
            curr = evenEdits
            prev = oddEdits
        curr[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j - 1], prev[j], curr[j - 1]
                )
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]
