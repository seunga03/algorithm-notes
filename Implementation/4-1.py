''' 상하좌우
NxN 크기의 공간이 있고, 사용자가 (1, 1) 좌표에서 출발
L(왼쪽), R(오른쪽), U(위), D(아래)로 이루어진 이동 계획이 문자열로 주어짐
이때, 공간을 벗어나는 이동은 무시하며, 최종 위치를 구하기
'''

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)