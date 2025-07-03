''' 게임 개발
게임 캐릭터가 맵 위를 이동하도록 프로그래밍하려고 한다.
캐릭터는 다음 규칙에 따라 이동한다:
- 맵 정보
N x M 크기의 직사각형 맵이 주어짐 (바다와 육지로 구성)
맵의 각 칸은 0(육지) 또는 1(바다) 로 표시됨
- 캐릭터의 초기 상태
캐릭터의 시작 좌표 (x, y)와 방향이 주어짐
방향은 0: 북, 1: 동, 2: 남, 3: 서
－ 이동 규칙
현재 방향 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정함
왼쪽에 가보지 않은 육지가 있으면, 왼쪽 방향으로 방향 전환 → 한 칸 전진 → 방문 체크
네 방향 모두 이미 가봤거나 바다일 경우, 뒤로 한 칸 이동 (방향은 유지)
뒤가 바다이면 이동을 종료함
'''

n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 위치 방문 처리

# 맵 정보 입력받기
visited = []
for i in range(n):
    visited.append(list(map(int, input().split())))

# 방향 설정: 북 동 남 서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 가보지 않은 + 육지인 경우
    if d[nx][ny] == 0 and visited[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    # 가봤거나 + 바다인 경우
    else:
        turn_time += 1

    # 사방이 가봤거나 + 바다인 경우 -> 뒤로 이동
    if turn_time == 4:
        # 뒤로 이동
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤에 육지가 있다면 이동만 하고 루프 계속
        if visited[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다라면 종료
        else:
            break
        turn_time = 0

print(count)