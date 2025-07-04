# Generated by Mochi Python compiler
from __future__ import annotations

import dataclasses
import typing

def newQueue() -> MyQueue:
	return MyQueue(ins=[], outs=[])

def push(q: MyQueue, x: int) -> MyQueue:
	s = q.ins
	s = (s + [x])
	return MyQueue(ins=s, outs=q.outs)

def ensureOut(q: MyQueue) -> MyQueue:
	inStack = q.ins
	outStack = q.outs
	if (len(outStack) == 0):
		while (len(inStack) > 0):
			v = inStack[(len(inStack) - 1)]
			inStack = inStack[0:(len(inStack) - 1)]
			outStack = (outStack + [v])
	return MyQueue(ins=inStack, outs=outStack)

def pop(q: MyQueue) -> PopResult:
	shifted = ensureOut(q)
	outStack = shifted.outs
	v = outStack[(len(outStack) - 1)]
	outStack = outStack[0:(len(outStack) - 1)]
	newQ = MyQueue(ins=shifted.ins, outs=outStack)
	return PopResult(queue=newQ, val=v)

def peek(q: MyQueue) -> int:
	shifted = ensureOut(q)
	return shifted.outs[(len(shifted.outs) - 1)]

def empty(q: MyQueue) -> bool:
	return ((len(q.ins) == 0) and (len(q.outs) == 0))

@dataclasses.dataclass
class MyQueue:
	ins: list[int]
	outs: list[int]

@dataclasses.dataclass
class PopResult:
	queue: MyQueue
	val: int

def example():
	q = newQueue()
	q = push(q, 1)
	q = push(q, 2)
	assert (peek(q) == 1)
	r1 = pop(q)
	q = r1.queue
	assert (r1.val == 1)
	assert (empty(q) == False)

def multiple_operations():
	q = newQueue()
	q = push(q, 3)
	q = push(q, 4)
	r1 = pop(q)
	q = r1.queue
	assert (r1.val == 3)
	q = push(q, 5)
	assert (peek(q) == 4)
	r2 = pop(q)
	q = r2.queue
	assert (r2.val == 4)
	r3 = pop(q)
	q = r3.queue
	assert (r3.val == 5)
	assert (empty(q) == True)

def main():
	example()
	multiple_operations()

if __name__ == "__main__":
	main()
