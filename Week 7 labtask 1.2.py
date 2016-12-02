def dfs(graph, start, path=[]):
  q=[start] # begin the search from the start of graph 
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

graph = { "A" : ["C", "B"],
          "B" : ["A", "C"],
          "C" : ["B", "D"],
          "D" : ["C", "E"],
          "E" : ["D", "F"],
          "F" : ["E"]} 


print 'Depth first search =', dfs(graph, 'A')
