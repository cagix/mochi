# Generated by Mochi Python compiler
from __future__ import annotations

import dataclasses
import typing

def newNumArray(values: list[int]) -> NumArray:
	return NumArray(nums=values)

def update(arr: NumArray, index: int, val: int) -> NumArray:
	data = arr.nums
	data[index] = val
	return NumArray(nums=data)

def sumRange(arr: NumArray, left: int, right: int) -> int:
	i = left
	total = 0
	while (i <= right):
		total = (total + arr.nums[i])
		i = (i + 1)
	return total

@dataclasses.dataclass
class NumArray:
	nums: list[int]

def example():
	na = newNumArray([1, 3, 5])
	assert (sumRange(na, 0, 2) == 9)
	na = update(na, 1, 2)
	assert (sumRange(na, 0, 2) == 8)

def update_first_and_last():
	na = newNumArray([2, 4, 6, 8])
	na = update(na, 0, 1)
	na = update(na, 3, 5)
	assert (sumRange(na, 0, 3) == 16)
	assert (sumRange(na, 1, 2) == 10)

def main():
	example()
	update_first_and_last()

if __name__ == "__main__":
	main()
