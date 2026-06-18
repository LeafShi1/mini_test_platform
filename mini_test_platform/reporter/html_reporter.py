# reporter/html_reporter.py

def generate_report(results, summary, output_file):

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("<html><body>")
        f.write("<h1>Test Report</h1>")

        f.write("<h2>Summary</h2>")
        f.write(f"<p>Total: {summary['Total']}</p>")
        f.write(f"<p>Passed: {summary['Passed']}</p>")
        f.write(f"<p>Failed: {summary['Failed']}</p>")
        f.write(f"<p>Pass Rate: {summary['Pass Rate']:.2f}%</p>")
        f.write(f"<p> Execution Time: {summary['Execution Time']:.3f}s</p>")

        f.write("<h2>Details</h2>")
        for r in results:
            color = "green" if r["success"] else "red"
            f.write(f"<p style='color:{color}'>")

            status =("PASS" if r["success"] else 'FAIL')

            f.write(f"{r['name']}: {status} {r['duration']:.3f}s")
            f.write("</p>")

        f.write("</body></html>")