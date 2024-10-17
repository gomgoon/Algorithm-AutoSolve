def solution(tickets):
    answer = []
    tickets.sort()
    visited = [False for _ in range(len(tickets)+ 1)]
    
    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            tmp = [ticket[0], ticket[1]]
            visited[idx] = True
            route = dfs(ticket, tickets, visited, tmp)
            if len(route) == len(tickets)+1:
                answer.append(route)
            visited[idx] = False
            
    answer.sort()
    return answer[0]

def dfs(ticket, tickets, visited, route):
    if len(route) == len(tickets)+1:
        return route
    for idx, t in enumerate(tickets):
        if t[0] == ticket[1] and visited[idx] == False:
            visited[idx] = True
            route.append(t[1])
            result = dfs(t, tickets, visited, route)
            
            if result:
                return result
            
            route.pop()
            visited[idx] = False
            
    return []