# Uses python3
import sys
from collections import namedtuple
from operator import itemgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    length = len(segments)
    segments = sorted(segments,key=itemgetter(Segment._fields.index('end')))
    i = 0
    while i < length:
        p = segments[i].end
        for s in segments[i+1:]:
            if s.start<=p<=s.end:
                i+=1
            else:
                break
        points.append(p)
        i+=1

    return set(points)
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
