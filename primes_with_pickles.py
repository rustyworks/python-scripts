import argparse
import pickle


FILE_LOCATION = 'primes_pkl/primes.pkl'


def load_primes():
    with open(FILE_LOCATION, 'rb') as f:
        primes = pickle.load(f)
    return primes


def dump_primes(primes):
    with open(FILE_LOCATION, 'wb') as f:
        pickle.dump(primes, f)


def generate_primes(primes, up_to):
    primes_ = primes[:]

    for i in range(primes[-1], up_to):
        for prime in primes_[:len(primes_) // 2]:
            if i % prime == 0:
                break
        else:
            primes_.append(i)

    return primes_


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate and Dump primes')
    parser.add_argument(
        '--up-to',
        dest='up_to',
        type=int,
        default=1000,
        help='generate primes up to n')
    args = parser.parse_args()
    up_to = args.up_to

    primes = [2, 3, 5]

    try:
        primes = load_primes()
    except FileNotFoundError:
        primes = generate_primes(primes, up_to)
        dump_primes(primes)

    if primes[-1] < up_to:
        primes = generate_primes(primes, up_to)
        dump_primes(primes)

    filtered_primes = list(filter(lambda x: x < up_to, primes))
    print(filtered_primes[-1])
