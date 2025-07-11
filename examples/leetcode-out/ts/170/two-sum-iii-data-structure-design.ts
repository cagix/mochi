// Generated by Mochi TypeScript compiler

type TwoSum = {
  counts: Record<number, number>;
};

function newTwoSum(): TwoSum {
  return { counts: {} };
}

function add(ts: TwoSum, number: number): TwoSum {
  let counts: Record<number, number> = ts.counts;
  (globalThis as any).counts = counts;
  let current: number = 0;
  (globalThis as any).current = current;
  if (Object.prototype.hasOwnProperty.call(counts, String(number))) {
    current = counts[number];
  }
  counts[number] = current + 1;
  return { counts: counts };
}

function find(ts: TwoSum, value: number): boolean {
  for (const keyKey of Object.keys(ts.counts)) {
    const key: number = Number(keyKey);
    let count: number = ts.counts[key];
    (globalThis as any).count = count;
    let complement: number = value - key;
    (globalThis as any).complement = complement;
    if (Object.prototype.hasOwnProperty.call(ts.counts, String(complement))) {
      let other: number = ts.counts[complement];
      (globalThis as any).other = other;
      if ((key != complement)) {
        return true;
      } else {
        if ((other > 1)) {
          return true;
        }
      }
    }
  }
  return false;
}

function test_example(): void {
  let ts: TwoSum = newTwoSum();
  (globalThis as any).ts = ts;
  ts = add(ts, 1);
  ts = add(ts, 3);
  ts = add(ts, 5);
  if (!(find(ts, 4) == true)) throw new Error("expect failed");
  if (!(find(ts, 7) == false)) throw new Error("expect failed");
}

function test_duplicate_numbers(): void {
  let ts: TwoSum = newTwoSum();
  (globalThis as any).ts = ts;
  ts = add(ts, 2);
  ts = add(ts, 2);
  if (!(find(ts, 4) == true)) throw new Error("expect failed");
  if (!(find(ts, 3) == false)) throw new Error("expect failed");
}

function main(): void {
  test_example();
  test_duplicate_numbers();
}
main();
