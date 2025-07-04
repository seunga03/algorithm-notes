''' 거스름돈
동전은 무한히 존재: 500원, 100원, 50원, 10원
손님에게 거슬러 줘야 할 돈: N원 (N은 항상 10의 배수)
거슬러 줘야 할 동전의 최소 개수 구하기
'''
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n = n % coin

print(count)

# 화폐의 종류가 K개라고 할 때 시간 복잡도: O(K)
# 동전의 총 종류에만 영향을 받고,
# 거슬러 줘야 하는 금액의 크기와는 무관하다.
