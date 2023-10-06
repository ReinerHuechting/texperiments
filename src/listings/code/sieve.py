# The Sieve of Eratosthenes

def sieve(n):
    """Return a list of all prime numbers less than n."""
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, n):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return [i for i, p in enumerate(primes) if p]

def main():
    print(sieve(100))

if __name__ == '__main__':
    main()
