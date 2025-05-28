def generate_abacaba_sequence(depth):
    if depth < 0:
        return ""
    if depth == 0:
        return "A"
    prev = generate_abacaba_sequence(depth - 1)
    letter = chr(ord("A") + depth)
    return prev + letter + prev

def is_abacaba_like(sequence):
    def check(seq):
        if len(seq) <= 1:
            return True
        mid = len(seq) // 2
        return seq[:mid] == seq[mid+1:] and check(seq[:mid])
    return check(sequence)
