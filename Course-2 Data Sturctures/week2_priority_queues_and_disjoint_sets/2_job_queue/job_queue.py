# python3
from collections import namedtuple
from math import floor
from collections import deque

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def parent(pt):
    return floor((pt-1)/2)

def sift_up(pt):
    while pt>0 and working_time[busy_workers[parent(pt)]] > working_time[busy_workers[pt]]:
        busy_workers[parent(pt)], busy_workers[pt] = busy_workers[pt], busy_workers[parent(pt)]
        pt = parent(pt) 

def sift_down(pt):
    size = len(busy_workers)
    minIndex = pt
    l = (2*pt)+1
    r = (2*pt)+2
    if l<size:
        if working_time[busy_workers[l]] < working_time[busy_workers[minIndex]]:
            minIndex = l  
        elif working_time[busy_workers[l]] == working_time[busy_workers[minIndex]]:
            if busy_workers[l] < busy_workers[minIndex]:
                minIndex = l
            if r<size:
                if working_time[busy_workers[r]] == working_time[busy_workers[minIndex]]:
                    pop_root = busy_workers.popleft()
                    busy_workers.append(pop_root)
                    sift_up(len(busy_workers)-1)
                    return 
            else:
                pass
        if r<size:
            if working_time[busy_workers[r]] < working_time[busy_workers[minIndex]]:
                minIndex = r
            elif working_time[busy_workers[r]] == working_time[busy_workers[minIndex]]:
                if busy_workers[l]<busy_workers[r]:
                    minIndex = l
                else:
                    minIndex = r

    # simple case 
    if pt!=minIndex:    
        busy_workers[pt], busy_workers[minIndex] = busy_workers[minIndex], busy_workers[pt]
        sift_down(minIndex)


def take_job(pt):
    thread_index = busy_workers[0]
    started_at = working_time[thread_index]
    working_time[thread_index] += jobs[pt]
    sift_down(0)
    return thread_index, started_at

def assign_jobs(n_workers, jobs):
    result = []
    for job in range(len(jobs)):
        next_worker, started_at = take_job(job)
        result.append(AssignedJob(next_worker, started_at))
    return result

if __name__ == "__main__":
    n_workers, n_jobs = map(int, input().split())
    working_time = [0 for i in range(n_workers)]
    busy_workers = deque([i for i in range(n_workers)])
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)
    for job in assigned_jobs:
        print(job.worker, job.started_at)