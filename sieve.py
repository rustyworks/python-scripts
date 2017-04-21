#!/usr/bin/python3

import argparse


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
    # TODO: Optimize using cache because recursive is expensive
    # TODO: Try use flag instead of append

    parser = argparse.ArgumentParser(description='Generate the primes')
    parser.add_argument('--get', dest='get', type=int)
    parser.add_argument('--find', dest='find_n', type=int)
    parser.add_argument('--list', nargs='?', type=int)

    args = parser.parse_args()

    prime = Prime()
    if args.get:
        print(prime.get(args.get))
    if args.find_n:
        print(prime.find_n(args.find_n))
    if args.list:
        print(prime.primes[:args.list])
