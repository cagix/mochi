# Generated by Mochi Python compiler
from __future__ import annotations

import typing

def containsDuplicate(nums: list[int]) -> bool:
	seen = {}
	for n in nums:
		if (n in seen):
			return True
		seen[n] = True
	return False

def example_1():
	assert (containsDuplicate([1, 2, 3, 1]) == True)

def example_2():
	assert (containsDuplicate([1, 2, 3, 4]) == False)

def example_3():
	assert (containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)

def main():
	example_1()
	example_2()
	example_3()

if __name__ == "__main__":
	main()
