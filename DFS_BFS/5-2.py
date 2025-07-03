''' 큐
선입선출 구조
파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용한다
(대부분의 코테에서 collections 모듈과 같은 기본 라이브러리 사용을 허용함)
deque: 스택과 큐의 장점을 모두 채택한 것.
       데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적.
       queue 라이브러리를 이용하는 것보다 더 간단.
deque 객체를 리스트 자료형으로 변경하고자 한다면 list() 메서드를 이용하면 된다
'''

from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)