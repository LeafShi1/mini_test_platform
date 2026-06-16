
def generate_reporter(results, output = "report.html"):
  with open(output, "w") as f:
    f.write("<html><body>")
    f.write("<h1>Test Report</h1>")

    for r in results:
      color = "green" if r["success"] else "red"
      f.write(f"<p style='color:{color}'")
      f.write(f"{r['name']}: {'PASS' if r['success'] else 'FAIL'}")
      f.write(f"</p>")


      f.write("</body></html>")


