# runner/test_runner.py

import logging

logger = logging.getLogger(__name__)


def add(a, b):
    return a + b

def run_tests(test_cases):
    results = []

    for case in test_cases:
        
        logger.info(f"Running {case['name']}")

        try:
            actual = add(*case["input"])
            success = actual == case["expected"]
        except Exception as ex:
            logger.exception(f"{case['name']} exception")

            success = False
            actual = str(ex)

        if success:
            logger.info(f"{case['name']} PASSED")
        else:
            logger.error(
                f"{case['name']} FAILED"
                f"(expected = {case['expected']},"
                f"actual={actual})"
            )

        results.append({
            "name": case["name"],
            "expected": case["expected"],
            "actual": actual,
            "success": success
        })

    return results