def calculate_probabilities(sequence):
    if not sequence:
        return {}
    total = len(sequence)
    freq = {}
    for num in sequence:
        freq[num] = freq.get(num, 0) + 1
    return {k: v / total for k, v in freq.items()}
