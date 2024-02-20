#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__max) == 0:
            self.__max.append(a)
        else:
            max_num = self.__max[-1]
            if max_num <= a:
                self.__max.append(a)
            else:
                self.__max.append(max_num)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__max.pop()
        


    def Max(self):
        assert(len(self.__stack))
        return self.__max[len(self.__max)-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
