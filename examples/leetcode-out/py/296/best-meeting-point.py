# Generated by Mochi Python compiler
from __future__ import annotations

import typing

def abs(x: int) -> int:
	if (x < 0):
		return (-x)
	else:
		return x

def minTotalDistance(grid: list[list[int]]) -> int:
	rows = []
	cols = []
	i = 0
	while (i < len(grid)):
		j = 0
		row = grid[i]
		while (j < len(row)):
			if (row[j] == 1):
				rows = (rows + [i])
				cols = (cols + [j])
			j = (j + 1)
		i = (i + 1)
	sortedRows = [ r for r in sorted([ r for r in rows ], key=lambda r: r) ]
	sortedCols = [ c for c in sorted([ c for c in cols ], key=lambda c: c) ]
	mid = (len(sortedRows) // 2)
	rowMedian = sortedRows[mid]
	colMedian = sortedCols[mid]
	dist = 0
	k = 0
	while (k < len(sortedRows)):
		dist = (dist + abs((sortedRows[k] - rowMedian)))
		k = (k + 1)
	k = 0
	while (k < len(sortedCols)):
		dist = (dist + abs((sortedCols[k] - colMedian)))
		k = (k + 1)
	return dist

def example_1():
	assert (minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]) == 6)

def example_2():
	assert (minTotalDistance([[1, 1]]) == 1)

def single_column():
	assert (minTotalDistance([[1], [1]]) == 1)

def single_cell():
	assert (minTotalDistance([[1]]) == 0)

def main():
	example_1()
	example_2()
	single_column()
	single_cell()

if __name__ == "__main__":
	main()
