def build_summary(results, duration):
    total =len(results)
    passed = sum(1 for r in results if r["success"])
    failed= total - passed
    pass_rate= (passed / total)*100 if total >0 else 0

    return {
        "Total": total,
        "Passed": passed,
        "Failed": failed,
        "Pass Rate": pass_rate,
        "Execution Time": duration
      }