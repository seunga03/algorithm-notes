''' 왕실의 나이트
8×8 좌표 평면(체스판)이 있음
나이트가 한 칸에 존재하고, 위치는 예: a1, c2, d4 등으로 주어짐
나이트는 다음과 같이 총 8가지 방향으로 이동할 수 있음
    2칸 이동 + 1칸 수직 or 수평 이동 -> 총 8가지 경우의 수
나이트의 현재 위치가 주어졌을 때, 체스판을 벗어나지 않고 이동할 수 있는 경우의 수를 구하기
'''

input = input()

y = ord(input[0]) - ord('a') + 1
x = int(input[1])

steps = [(2,1), (2,-1), (-2,1), (-2,-1),
         (1,2), (1,-2), (-1,2), (-1,-2)]

count = 0
for dx, dy in steps:
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)