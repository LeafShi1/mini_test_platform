# reporter/html_reporter.py

def generate_report(results, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("<html><body>")
        f.write("<h1>Test Report</h1>")

        for r in results:
            color = "green" if r["success"] else "red"
            f.write(f"<p style='color:{color}'>")

            status =("PASS" if r["success"] else 'FAIL')

            f.write(f"{r['name']}: {status}")
            f.write("</p>")

        f.write("</body></html>")