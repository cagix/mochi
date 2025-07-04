# Generated by Mochi Python compiler
from __future__ import annotations

import dataclasses
import typing

def newLogger() -> Logger:
	return Logger(log={})

def shouldPrintMessage(logger: Logger, timestamp: int, message: str) -> PrintResult:
	log = logger.log
	if (message in log):
		last = log[message]
		if ((timestamp - last) < 10):
			return PrintResult(ok=False, logger=Logger(log=log))
	log[message] = timestamp
	return PrintResult(ok=True, logger=Logger(log=log))

@dataclasses.dataclass
class Logger:
	log: dict[str, int]

@dataclasses.dataclass
class PrintResult:
	ok: bool
	logger: Logger

def example():
	l = newLogger()
	r1 = shouldPrintMessage(l, 1, "foo")
	assert (r1.ok == True)
	l = r1.logger
	r2 = shouldPrintMessage(l, 2, "bar")
	assert (r2.ok == True)
	l = r2.logger
	r3 = shouldPrintMessage(l, 3, "foo")
	assert (r3.ok == False)
	l = r3.logger
	r4 = shouldPrintMessage(l, 8, "bar")
	assert (r4.ok == False)
	l = r4.logger
	r5 = shouldPrintMessage(l, 10, "foo")
	assert (r5.ok == False)
	l = r5.logger
	r6 = shouldPrintMessage(l, 11, "foo")
	assert (r6.ok == True)

def main():
	example()

if __name__ == "__main__":
	main()
