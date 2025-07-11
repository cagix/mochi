# Generated by Mochi Python compiler
from __future__ import annotations

import dataclasses
import typing

def newRandomPicker(values: list[int], seed: int) -> RandomPicker:
	return RandomPicker(values=values, seed=seed)

def nextSeed(seed: int) -> int:
	return ((((seed * 1103515245) + 12345)) % 2147483648)

def getRandom(p: RandomPicker) -> PickResult:
	seed2 = nextSeed(p.seed)
	idx = (seed2 % len(p.values))
	np = RandomPicker(values=p.values, seed=seed2)
	return PickResult(picker=np, value=p.values[idx])

@dataclasses.dataclass
class RandomPicker:
	values: list[int]
	seed: int

@dataclasses.dataclass
class PickResult:
	picker: RandomPicker
	value: int

def single_element():
	p = newRandomPicker([5], 1)
	r1 = getRandom(p)
	assert (r1.value == 5)
	r2 = getRandom(r1.picker)
	assert (r2.value == 5)

def deterministic_sequence():
	p = newRandomPicker([10, 20, 30], 42)
	r1 = getRandom(p)
	assert (r1.value == 10)
	p = r1.picker
	r2 = getRandom(p)
	assert (r2.value == 30)
	p = r2.picker
	r3 = getRandom(p)
	assert (r3.value == 30)

def main():
	single_element()
	deterministic_sequence()

if __name__ == "__main__":
	main()
