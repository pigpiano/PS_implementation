

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
#양방향 연결리스트 생성을 위한 deque
q = deque([i for i in range(1, n+1)])

arr = []
while len(q) != 0:
    # k-1번째까지의 값들을 맨 뒤로 보낸다.
    for i in range(k-1):
        q.append(q.popleft())
    # k번째 요소를 제거한다.
    arr.append(str(q.popleft()))

#결과 출력, '구분자'.join(리스트) -> 문자열 결합
#ex '_'join(['a','b','c']) => "a_b_c"
print('<' + ', '.join(arr) + '>')