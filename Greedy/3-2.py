''' 큰 수의 법칙
N개의 숫자로 이루어진 배열이 주어짐
총 M번 숫자를 더할 수 있음
단, 특정 인덱스의 숫자를 연속해서 K번을 초과하여 더할 수 없음
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[-1]
second = data[-2]

result = 0

count = m // (k+1) * k + m % (k+1)
result += count * first
result += (m - count) * second

print(result)