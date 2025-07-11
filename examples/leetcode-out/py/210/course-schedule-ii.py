# Generated by Mochi Python compiler
from __future__ import annotations

import typing

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
	graph = {}
	indegree = {}
	i = 0
	while (i < numCourses):
		graph[i] = []
		indegree[i] = 0
		i = (i + 1)
	for pair in prerequisites:
		dest = pair[0]
		src = pair[1]
		graph[src] = (graph[src] + [dest])
		indegree[dest] = (indegree[dest] + 1)
	queue = []
	j = 0
	while (j < numCourses):
		if (indegree[j] == 0):
			queue = (queue + [j])
		j = (j + 1)
	order = []
	while (len(queue) > 0):
		_next = []
		for course in queue:
			order = (order + [course])
			for neighbor in graph[course]:
				indegree[neighbor] = (indegree[neighbor] - 1)
				if (indegree[neighbor] == 0):
					_next = (_next + [neighbor])
		queue = _next
	if (len(order) == numCourses):
		return order
	return []

def example_1():
	assert (findOrder(2, [[1, 0]]) == [0, 1])

def example_2():
	order = findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
	valid = True
	if (len(order) == 4):
		idx = {}
		k = 0
		while (k < len(order)):
			idx[order[k]] = k
			k = (k + 1)
		if ((idx[0] > idx[1]) and (idx[0] > idx[2])):
			valid = False
		if (idx[1] > idx[3]):
			valid = False
		if (idx[2] > idx[3]):
			valid = False
	else:
		valid = False
	assert (valid == True)

def cycle():
	assert (findOrder(2, [[0, 1], [1, 0]]) == [])

def main():
	example_1()
	example_2()
	cycle()

if __name__ == "__main__":
	main()
