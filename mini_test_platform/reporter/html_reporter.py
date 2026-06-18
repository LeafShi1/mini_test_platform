# reporter/html_reporter.py

def generate_report(results, output_file, duration):

    total = len(results)
    passed = sum(1 for r in results if r["success"])
    failed = total- passed

    pass_rate = (passed / total)*100 if total >0 else 0

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("<html><body>")
        f.write("<h1>Test Report</h1>")

        f.write("<h2>Summary</h2>")
        f.write(f"<p>Total: {total}</p>")
        f.write(f"<p>Passed: {passed}</p>")
        f.write(f"<p>Failed: {failed}</p>")
        f.write(f"<p>Pass Rate: {pass_rate:.2f}%</p>")
        f.write(f"<p> Execution Time: {duration:.3f}s</p>")

        f.write("<h2>Details</h2>")
        for r in results:
            color = "green" if r["success"] else "red"
            f.write(f"<p style='color:{color}'>")

            status =("PASS" if r["success"] else 'FAIL')

            f.write(f"{r['name']}: {status}")
            f.write("</p>")

        f.write("</body></html>")