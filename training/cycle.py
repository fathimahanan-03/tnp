from collections import defaultdict

edges = defaultdict(list)
n = int(input()) 

for _ in range(n):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)  

visited = set()

def has_cycle(node, parent):
    visited.add(node)
    for neighbor in edges[node]:
        if neighbor not in visited:
            if has_cycle(neighbor, parent=node):
                return True
        elif neighbor != parent:
            return True
    return False

cycle_found = False
for node in edges:
    if node not in visited:
        if has_cycle(node, -1):
            cycle_found = True
            break

print(cycle_found)
