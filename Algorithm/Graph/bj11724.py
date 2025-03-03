import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

# 방문처리와 노드 입력받음
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

# 연결요소
cnt = 0

# 연결노드는 1처리
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS Stack
def dfs_stack(v):

    # stack에 삽입
    stack = [v]

    # stack이 empty일때까지
    while stack:

        # 가장 최근 요소 pop
        v = stack.pop()

        # 방문하지 않았다면 방문처리하고 연결 노드 stack에 삽입
        if visited[v] == 0:
            visited[v] = 1
            for i in graph[v]:
                stack.append(i)

# DFS 재귀
def dfs(v):

    # 방문처리
    visited[v] = 1

    # 연결노드에 방문하지 않았으면, 재귀
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
    
# 방문하지 않은 노드만 cnt + 1    
for i in range(1, n+1):
    if visited[i] == 0:
        dfs_stack(i)
        cnt+=1
print(cnt)