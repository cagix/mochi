# Generated by Mochi Python compiler
from __future__ import annotations

import typing

def removeElements(nums: list[int], val: int) -> list[int]:
	result = []
	for x in nums:
		if (x != val):
			result = (result + [x])
	return result

def example_1():
	assert (removeElements([1, 2, 6, 3, 4, 5, 6], 6) == [1, 2, 3, 4, 5])

def example_2():
	assert (removeElements([], 1) == [])

def example_3():
	assert (removeElements([7, 7, 7, 7], 7) == [])

def no_removals():
	assert (removeElements([1, 2, 3], 4) == [1, 2, 3])

def all_removed():
	assert (removeElements([2, 2, 2], 2) == [])

def main():
	example_1()
	example_2()
	example_3()
	no_removals()
	all_removed()

if __name__ == "__main__":
	main()
