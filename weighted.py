# -*- coding: utf-8 -*-
#%%
graph = {
    "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
    "b": [{"node": "d", "weight": 3}],
    "c": [{"node": "d", "weight": 1}],
    "d": [{"node": "e", "weight": 3}],
    "e": [],
    "f": []
}

def find_path(graph, start, end, path=[], weight=0):
    path = path + [{"node": start, "weight": weight}]
    if start == end:
        return path
    if not start in graph:
        return None
    for conn in graph[start]:
        if conn["node"] not in path:
            newpath = find_path(graph, conn["node"], end, path, conn["weight"])
            if newpath is not None:
                return newpath
    return None

def find_all_paths(graph, start, end, path=[], weight=0):
    path = path + [{"node": start, "weight": weight}]

    if start == end:
        return [path]

    if not start in graph:
        return []

    paths = []
    
    for conn in graph[start]:
        if conn not in path:
            newpaths = find_all_paths(graph, conn["node"], end, path, conn["weight"])
            
            for newpath in newpaths:
                paths.append(newpath)

    return paths

def cheapest_path(graph, start, end):
    all_paths = find_all_paths(graph, start, end)
    
    cheapest = None
    
    for path in all_paths:
        cost = 0
        
        for step in path:
            cost += step["weight"]
            
        if cheapest is None or cost < cheapest:
            cheapest = cost
            
    return cheapest