# runner/test_runner.py

def add(a, b):
    return a + b

def run_tests(test_cases):
    results = []

    for case in test_cases:
        actual = add(*case["input"])
        success = actual == case["expected"]

        results.append({
            "name": case["name"],
            "expected": case["expected"],
            "actual": actual,
            "success": success
        })

    return results