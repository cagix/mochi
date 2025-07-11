// Generated by Mochi TypeScript compiler

function titleToNumber(columnTitle: string): number {
  let values: Record<string, number> = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
  };
  (globalThis as any).values = values;
  let result: number = 0;
  (globalThis as any).result = result;
  for (const ch of columnTitle) {
    result = (result * 26) + values[ch];
  }
  return result;
}

function test_example_1(): void {
  if (!(titleToNumber("A") == 1)) throw new Error("expect failed");
}

function test_example_2(): void {
  if (!(titleToNumber("AB") == 28)) throw new Error("expect failed");
}

function test_example_3(): void {
  if (!(titleToNumber("ZY") == 701)) throw new Error("expect failed");
}

function test_single_Z(): void {
  if (!(titleToNumber("Z") == 26)) throw new Error("expect failed");
}

function test_large_input(): void {
  if (!(titleToNumber("FXSHRXW") == 2147483647)) {
    throw new Error("expect failed");
  }
}

function main(): void {
  test_example_1();
  test_example_2();
  test_example_3();
  test_single_Z();
  test_large_input();
}
main();
