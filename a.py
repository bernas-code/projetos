import itertools

charset = "abc123"
max_length = 3

for length in range(1, max_length + 1):
    for attempt in itertools.product(charset, repeat=length):
        print(''.join(attempt))