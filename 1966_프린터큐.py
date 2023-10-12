

# 큐 자료구조 사용하기 위해 덱 라이브러리 가져오기
from collections import deque
import sys
input = sys.stdin.readline

# 입력받기
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    # 큐 구현을 위한 deque 라이브러리 사용
    q = deque()
    # m번 째 위치 값의 출력 순서를 확인하기 위해, 중요도와 index 위치값을 결합해서 큐에 삽입
    for i in range(n):
        q.append((priority[i], i))

    # 우선 순위가 가장 높은 것부터 빼기 떄문에 정렬한다
    priority.sort(reverse=True)
    count = 1 # 출력 순서 처음에 1로 초기화
    while q:
        now = q.popleft()
        if now[0] == priority[count-1]:
            if now[1] == m: # 찾는 위치의 값일 라면
                print(count)
                break
            count += 1 # 출력 순서 업데이트
        else:
            # 꺼낸 값이 최고값이 아니라면 뒤로 옮긴다.
            q.append(now)


