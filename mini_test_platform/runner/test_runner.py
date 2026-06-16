
from unittest import result


def add(a, b):
  return a + b

def run_tests(test_cases):
  results = []

  for case in test_cases:
    actual = add(*case["input"])
    success = actual == case["expected"]

    results.append({"input": case["input"], "expected": case["expected"], "actual": actual, "success": success})

  return results



