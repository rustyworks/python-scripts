#!/usr/bin/python3


class Prime():
    '''
    Program to generate prime number using sieve of Eratosthenes
    '''

    def __init__(self):
        self.primes = [2]
        self.generate(10000)

    def get(self, prime_limit):
        '''
        This is to get the last prime number before the limit
        '''
        if self.primes[-1] <= prime_limit:
            self.generate(self.primes[-1] * self.primes[-1])
            return self.get(prime_limit)
        else:
            result =  [prime for prime in self.primes if prime <= prime_limit][-1]
            return result

    def find_n(self, prime_at):
        '''
        This is to get the n-th number of primes
        '''
        if len(self.primes) > prime_at:
            return self.primes[prime_at - 1]
        else:
            self.generate(self.primes[-1] * self.primes[-1])
            return self.find_n(prime_at)

    def generate(self, number_to_generate):
        numbers = self.primes + [num for num in range(self.primes[-1], number_to_generate + 1)]
        self.primes = []
        while numbers:
            self.primes.append(numbers[0])
            numbers = [num for num in numbers if num % self.primes[-1] != 0]

if __name__ == '__main__':
    # TODO: Support argsparse
    # TODO: Optimize using cache because recursive is expensive
    # TODO: Try use flag instead of append
    prime = Prime()
    print(prime.get(8888))
