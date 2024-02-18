import heapq

def solution(jobs):
    answer = 0
    time = 0
    job_count = len(jobs)
    heap = []
    
    jobs.sort(key = lambda x: x[0])
    print(jobs)
    
    while jobs or heap:
        while jobs and jobs[0][0] <= time:
            duration, execute = jobs.pop(0)
            heapq.heappush(heap, [execute, duration])
        
        if heap:
            temp = heapq.heappop(heap)
            t = time + temp[0] - temp[1]
            answer += t
            time += temp[0]
        else:
            time+=1
    
    return answer // job_count