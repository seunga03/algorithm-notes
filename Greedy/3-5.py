n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k
    count += n - target
    n = target

    if n < k:
        break

    n //= k
    count += 1

count += n - 1
print(count)