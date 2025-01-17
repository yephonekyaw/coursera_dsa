# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = ans*self._multiplier + ord(c)
            ans = ((ans % self._prime) + self._prime) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(cur for cur in reversed(self.elems[query.ind]))
        else:
            hash_value = self._hash_func(query.s)
            try:
                ind = self.elems[hash_value].index(query.s)
            except ValueError:
                ind = -1
            if query.type == "add":
                if ind == -1:
                    self.elems[hash_value].append(query.s)
            elif query.type == "del":
                if ind != -1:
                    self.elems[hash_value].pop(ind)
            else:
                self.write_search_result(ind != -1)



    def process_queries(self):
        n = int(input())
        for _ in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
    # print(proc.elems)