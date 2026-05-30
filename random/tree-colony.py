import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = [[] for _ in range(n + 1)]

        for _ in range(n - 1):
            u, v = map(int, input().split())
            edges[u].append(v)
            edges[v].append(u)

        # Step 1: compute depths using DFS
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)

        def dfs(u):
            for v in edges[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    dfs(v)

        dfs(1)

        # Step 2: group nodes by depth
        levels = {}
        for i in range(1, n + 1):
            d = depth[i]
            if d not in levels:
                levels[d] = []
            levels[d].append(i)

        # Step 3: minimum number of operations
        k = max(len(nodes) for nodes in levels.values())

        # Step 4: build operations
        ops = [[] for _ in range(k)]
        for d in levels:
            nodes = levels[d]
            for i in range(len(nodes)):
                ops[i].append(nodes[i])

        # Output
        print(k)
        for op in ops:
            print(len(op), *op)

if __name__ == "__main__":
    solve()
