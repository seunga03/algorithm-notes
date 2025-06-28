''' 숫자 카드 게임
N행 M열의 숫자 카드들이 2차원 배열 형태로 주어진다
각 행마다 숫자 중 가장 작은 수를 선택한다
그 중에서 가장 큰 수 하나를 골라야 한다
'''

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)