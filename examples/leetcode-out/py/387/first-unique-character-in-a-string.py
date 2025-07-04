# Generated by Mochi Python compiler
from __future__ import annotations

import typing

def firstUniqChar(s: str) -> int:
	counts = {}
	i = 0
	while (i < len(s)):
		ch = s[i]
		if (ch in counts):
			counts[ch] = (counts[ch] + 1)
		else:
			counts[ch] = 1
		i = (i + 1)
	i = 0
	while (i < len(s)):
		ch = s[i]
		if (counts[ch] == 1):
			return i
		i = (i + 1)
	return (-1)

def example_1():
	assert (firstUniqChar("leetcode") == 0)

def example_2():
	assert (firstUniqChar("loveleetcode") == 2)

def example_3():
	assert (firstUniqChar("aabb") == ((-1)))

def empty_string():
	assert (firstUniqChar("") == ((-1)))

def single_char():
	assert (firstUniqChar("z") == 0)

def main():
	example_1()
	example_2()
	example_3()
	empty_string()
	single_char()

if __name__ == "__main__":
	main()
