# DFS / BFS

## 1. 핵심 개념

DFS와 BFS는 **그래프나 트리의 정점을 탐색하는 대표적인 방법**이다.

```text
DFS = Depth-First Search
      깊이 우선 탐색

BFS = Breadth-First Search
      너비 우선 탐색
```

가장 중요한 차이는 **탐색 순서와 사용하는 자료구조**다.

```text
DFS → Stack / 재귀
BFS → Queue
```

---

## 2. 그래프 표현

코테에서는 보통 **인접 리스트**를 사용한다.

```python
n = 5
graph = [[] for _ in range(n)]

graph[0].append(1)
graph[1].append(0)

graph[0].append(2)
graph[2].append(0)
```

그래프:

```text
    1
   /
  0
   \
    2
```

---

# DFS

## 3. DFS란?

DFS는 **한 방향으로 최대한 깊게 들어간 뒤 더 갈 곳이 없으면 돌아오는 방식**이다.

```text
1 → 2 → 4
    ↓
    3
```

재귀 또는 스택으로 구현한다.

---

## 4. 재귀 DFS

가장 대표적인 형태:

```python
def dfs(node):
    visited[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)
```

호출:

```python
visited = [False] * n
dfs(0)
```

---

## 5. 스택을 이용한 DFS

재귀 대신 직접 스택을 사용할 수도 있다.

```python
stack = [start]
visited = [False] * n
visited[start] = True

while stack:
    node = stack.pop()

    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            stack.append(nxt)
```

핵심:

```python
stack.append(x)
stack.pop()
```

---

## 6. DFS 대표 활용

- 모든 정점 탐색
- 연결 요소 찾기
- 경로 존재 여부
- 백트래킹
- 사이클 탐지
- 조합/순열 탐색
- 트리 탐색

특히 **백트래킹**과 DFS가 자주 결합된다.

---

# BFS

## 7. BFS란?

BFS는 **현재 위치에서 가까운 정점부터 차례대로 탐색**한다.

```text
       1
      / \
     2   3
    / \
   4   5

탐색 순서:
1 → 2 → 3 → 4 → 5
```

큐를 사용한다.

---

## 8. Python BFS 기본 형태

`list.pop(0)` 대신 `deque`를 사용한다.

```python
from collections import deque

q = deque([start])
visited = [False] * n
visited[start] = True

while q:
    node = q.popleft()

    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
```

핵심:

```python
q.append(x)
q.popleft()
```

---

## 9. BFS와 최단거리

**모든 간선의 비용이 동일한 경우**, BFS는 최단거리 문제에 매우 강하다.

```python
from collections import deque

dist = [-1] * n
dist[start] = 0

q = deque([start])

while q:
    node = q.popleft()

    for nxt in graph[node]:
        if dist[nxt] == -1:
            dist[nxt] = dist[node] + 1
            q.append(nxt)
```

예를 들어:

```text
start → A → B → C
```

라면:

```text
start = 0
A     = 1
B     = 2
C     = 3
```

---

## 10. 격자/미로 BFS

코테에서 매우 자주 나온다.

```python
from collections import deque

q = deque([(0, 0)])
visited = [[False] * m for _ in range(n)]
visited[0][0] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
```

---

## 11. DFS vs BFS

| 구분 | DFS | BFS |
|---|---|---|
| 의미 | 깊이 우선 | 너비 우선 |
| 핵심 구조 | Stack | Queue |
| Python | 재귀/list | deque |
| 최단거리 | 일반적으로 부적합 | 가중치 동일 시 강함 |
| 백트래킹 | 자주 사용 | 거의 사용하지 않음 |
| 미로 탐색 | 가능 | 매우 자주 사용 |

---

## 12. 언제 DFS를 생각할까?

다음 표현이 나오면 DFS를 고려한다.

- 모든 경우를 탐색
- 가능한 경로를 모두 확인
- 조합/순열
- 백트래킹
- 연결 요소
- 트리의 깊이 있는 탐색

---

## 13. 언제 BFS를 생각할까?

다음 표현이 나오면 BFS를 고려한다.

- 최단 거리
- 최소 횟수
- 몇 단계 만에 도착
- 가까운 순서대로 탐색
- 미로
- 레벨별 탐색

단, 최단거리라도 **가중치가 다른 그래프**라면 BFS가 아니라 다익스트라 등을 고려해야 한다.

---

## 14. 방문 처리

그래프 탐색에서 가장 중요한 것 중 하나다.

```python
visited = [False] * n
```

방문하면:

```python
visited[node] = True
```

방문 여부를 확인:

```python
if not visited[nxt]:
    ...
```

격자에서는:

```python
visited = [[False] * m for _ in range(n)]
```

---

## 15. DFS/BFS 문제 풀이 순서

문제를 읽고 다음 순서로 생각한다.

```text
① 그래프인가?
      ↓
② 그래프를 어떻게 표현하지?
      ↓
③ 방문 처리가 필요한가?
      ↓
④ 깊게 탐색 → DFS
   가까운 순서/최단거리 → BFS
      ↓
⑤ 가중치가 있는가?
      ↓
   그렇다면 다익스트라 등 고려
```

---

## 16. 시간 복잡도

인접 리스트를 사용하면 DFS/BFS의 기본 탐색은:

```text
O(V + E)
```

- `V`: 정점 수
- `E`: 간선 수

각 정점과 간선을 필요한 만큼 확인하기 때문이다.

### 기억할 것

```text
DFS → 깊게 → Stack/재귀
BFS → 가까운 것부터 → Queue/deque
BFS + 동일 가중치 → 최단거리
그래프 + 가중치 최단거리 → 다익스트라 + heapq
```
