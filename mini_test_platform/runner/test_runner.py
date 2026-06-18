# runner/test_runner.py

import logging
import time

logger = logging.getLogger(__name__)


def add(a, b):
    return a + b

def run_tests(test_cases):
    results = []

    for case in test_cases:
        
        logger.info(f"Running {case['name']}")

        start_time= time.perf_counter()

        try:
            actual = add(*case["input"])
            success = actual == case["expected"]
        except Exception as ex:
            logger.exception(f"{case['name']} exception")

            success = False
            actual = str(ex)

        end_time = time.perf_counter()
        duration = end_time - start_time

        if success:
            logger.info(f"{case['name']} PASSED {duration:.3f}s")
        else:
            logger.error(
                f"{case['name']} FAILED  {duration:.3f}s"
                f"(expected = {case['expected']},"
                f"actual={actual})"
            )


        results.append({
            "name": case["name"],
            "expected": case["expected"],
            "actual": actual,
            "success": success,
            "duration": duration

        })

    return results