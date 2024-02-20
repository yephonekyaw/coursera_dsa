# python3
from collections import namedtuple

linkTableInfo = namedtuple("linkTableInfo", ["parent", "size"])
class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.size = [i for i in row_counts]
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            self.size[src_parent] += self.size[dst_parent]
            self.size[dst_parent] = 0
            if self.size[src_parent] > self.max_row_count:
                self.max_row_count = self.size[src_parent]
        else:
            self.parents[src_parent] = dst_parent
            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[dst_parent] += 1
            self.size[dst_parent] += self.size[src_parent]
            self.size[src_parent] = 0
            if self.size[dst_parent] > self.max_row_count:
                self.max_row_count = self.size[dst_parent] 
        return True

    def get_parent(self, table):
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]

def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for _ in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)
    
if __name__ == "__main__":
    main()