def find_parent(parent, x):
    # 부모 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] == x:
        return x
    # 경로 압축 최적화
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    # 각 노드의 부모를 찾음
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 번호가 작은 노드가 부모가 되도록 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 개수(v)와 간선 개수(e) 입력받기
v, e = map(int, input("노드 수와 간선 수를 입력하세요: ").split())

# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(v + 1)]

# Union 연산 수행
for _ in range(e):
    a, b = map(int, input("연결할 두 노드를 입력하세요: ").split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("\n각 원소가 속한 집합:")
for i in range(1, v + 1):
    print(f"노드 {i}: {find_parent(parent, i)}")

# 부모 테이블 출력
print("\n부모 테이블:")
for i in range(1, v + 1):
    print(f"노드 {i}: 부모 {parent[i]}")
    
    
# cycle 판별 소스 코드
cycle = False

for i in range(e) :
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b) : # 부모 노드 비교로 cycle 확인
        cycle = True
        break
    else :
        union_parent(parent, a, b)