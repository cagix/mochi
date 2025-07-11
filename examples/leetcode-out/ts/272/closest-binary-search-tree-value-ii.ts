// Generated by Mochi TypeScript compiler

function Leaf(): Record<string, any> {
  return { "__name": "Leaf" };
}

function _Node(
  left: Record<string, any>,
  value: number,
  right: Record<string, any>,
): Record<string, any> {
  return {
    "__name": "Node",
    "left": left,
    "value": value,
    "right": right,
  };
}

function isLeaf(t: Record<string, any>): boolean {
  return _equal(t["__name"], "Leaf");
}

function left(t: Record<string, any>): Record<string, any> {
  return t["left"];
}

function right(t: Record<string, any>): Record<string, any> {
  return t["right"];
}

function value(t: Record<string, any>): number {
  return t["value"];
}

function inorder(root: Record<string, any>): Array<number> {
  if (isLeaf(root)) {
    return [];
  }
  return inorder(left(root)).concat([value(root)]).concat(inorder(right(root)));
}

function absFloat(x: number): number {
  if ((x < 0)) {
    return (-x);
  } else {
    return x;
  }
}

function closestKValues(
  root: Record<string, any>,
  target: number,
  k: number,
): Array<number> {
  let vals: Array<number> = inorder(root);
  (globalThis as any).vals = vals;
  let sorted: Array<number> = (() => {
    const _src = vals;
    let _items = [];
    for (const v of _src) {
      _items.push(v);
    }
    let _pairs = _items.map((it) => {
      const v = it;
      return { item: it, key: absFloat(v - target) };
    });
    _pairs.sort((a, b) => {
      const ak = a.key;
      const bk = b.key;
      if (typeof ak === "number" && typeof bk === "number") return ak - bk;
      if (typeof ak === "string" && typeof bk === "string") {
        return ak < bk
          ? -1
          : (ak > bk ? 1 : 0);
      }
      return String(ak) < String(bk) ? -1 : (String(ak) > String(bk) ? 1 : 0);
    });
    _items = _pairs.map((p) => p.item);
    const _res = [];
    for (const v of _items) {
      _res.push(v);
    }
    return _res;
  })();
  (globalThis as any).sorted = sorted;
  return sorted.slice(0, k);
}

function test_example(): void {
  if (
    !(_equal(closestKValues(example, 3.714286, 2), [
      4,
      3,
    ]))
  ) throw new Error("expect failed");
}

function test_single_node(): void {
  if (!(_equal(closestKValues(_Node(Leaf(), 1, Leaf()), 0, 1), [1]))) {
    throw new Error("expect failed");
  }
}

function main(): void {
  let example: Record<string, any> = _Node(
    _Node(_Node(Leaf(), 1, Leaf()), 2, _Node(Leaf(), 3, Leaf())),
    4,
    _Node(Leaf(), 5, Leaf()),
  );
  (globalThis as any).example = example;
  test_example();
  test_single_node();
}
function _equal(a: any, b: any): boolean {
  if (Array.isArray(a) && Array.isArray(b)) {
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) if (!_equal(a[i], b[i])) return false;
    return true;
  }
  if (a && b && typeof a === "object" && typeof b === "object") {
    const ak = Object.keys(a);
    const bk = Object.keys(b);
    if (ak.length !== bk.length) return false;
    for (const k of ak) {
      if (!bk.includes(k) || !_equal((a as any)[k], (b as any)[k])) {
        return false;
      }
    }
    return true;
  }
  return a === b;
}

main();
