# Generated by Mochi Python compiler
from __future__ import annotations

import typing

def romanToInt(s: str) -> int:
	values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	total = 0
	i = 0
	n = len(s)
	while (i < n):
		curr = values[s[i]]
		if ((i + 1) < n):
			_next = values[s[(i + 1)]]
			if (curr < _next):
				total = ((total + _next) - curr)
				i = (i + 2)
				continue
		total = (total + curr)
		i = (i + 1)
	return total

def example_1():
	assert (romanToInt("III") == 3)

def example_2():
	assert (romanToInt("LVIII") == 58)

def example_3():
	assert (romanToInt("MCMXCIV") == 1994)

def subtractive():
	assert (romanToInt("IV") == 4)
	assert (romanToInt("IX") == 9)

def tens():
	assert (romanToInt("XL") == 40)
	assert (romanToInt("XC") == 90)

def main():
	example_1()
	example_2()
	example_3()
	subtractive()
	tens()

if __name__ == "__main__":
	main()
