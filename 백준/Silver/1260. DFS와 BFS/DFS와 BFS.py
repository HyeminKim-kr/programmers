from collections import deque, defaultdict
import sys
read = sys.stdin.readline

# DFS 함수 정의 (재귀 방식)
def dfs(v):
    visit_list[v] = True        
    print(v, end=" ")
    for neighbor in graph[v]:
        if not visit_list[neighbor]:
            dfs(neighbor)

# BFS 함수 정의 (큐 사용)
def bfs(v):
    queue = deque([v])
    visit_list[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for neighbor in graph[v]:
            if not visit_list[neighbor]:
                queue.append(neighbor)
                visit_list[neighbor] = True

n, m, v = map(int, read().split())

# 인접 리스트로 그래프 구축
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것부터 방문하기 위해 정렬
for key in graph:
    graph[key].sort()

# 방문 여부 리스트 초기화
visit_list = [False] * (n + 1)

# DFS 수행
dfs(v)
print()

# 방문 여부 리스트 재초기화
visit_list = [False] * (n + 1)

# BFS 수행
bfs(v)
print()
