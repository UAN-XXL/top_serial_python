def factorielle(n):
    return n * factorielle(n - 1) if n > 1 else 1
