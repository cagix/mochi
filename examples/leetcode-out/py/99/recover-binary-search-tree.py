# Generated by Mochi Python compiler
from __future__ import annotations

import dataclasses
import typing

def inorder(t: Tree) -> list[int]:
	return (lambda _t0=t: [] if isinstance(_t0, Leaf) else (lambda l, v, r: ((inorder(l) + [v]) + inorder(r)))(_t0.left, _t0.value, _t0.right) if isinstance(_t0, Node) else None)()

def recoverTree(t: Tree) -> Tree:
	vals = inorder(t)
	sortedVals = [ x for x in sorted([ x for x in vals ], key=lambda x: x) ]
	def build(lo: int, hi: int) -> Tree:
		if (lo >= hi):
			return Leaf()
		mid = (((lo + hi)) // 2)
		return Node(left=build(lo, mid), value=sortedVals[mid], right=build((mid + 1), hi))
	return build(0, len(sortedVals))

class Tree:
	pass
@dataclasses.dataclass
class Leaf(Tree):
	pass
@dataclasses.dataclass
class Node(Tree):
	left: Tree
	value: int
	right: Tree

ex = Node(left=Node(left=Leaf(), value=3, right=Leaf()), value=1, right=Node(left=Leaf(), value=4, right=Leaf()))
fixed = recoverTree(ex)
ex2 = Node(left=Node(left=Leaf(), value=2, right=Leaf()), value=4, right=Node(left=Leaf(), value=1, right=Leaf()))
fixed2 = recoverTree(ex2)

def main():
	ex = Node(left=Node(left=Leaf(), value=3, right=Leaf()), value=1, right=Node(left=Leaf(), value=4, right=Leaf()))
	fixed = recoverTree(ex)
	assert (inorder(fixed) == [1, 3, 4])
	ex2 = Node(left=Node(left=Leaf(), value=2, right=Leaf()), value=4, right=Node(left=Leaf(), value=1, right=Leaf()))
	fixed2 = recoverTree(ex2)
	assert (inorder(fixed2) == [1, 2, 4])

if __name__ == "__main__":
	main()
