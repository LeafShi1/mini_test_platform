# main.py
from loader.test_loader import load_tests
from runner.test_runner import run_tests
from reporter.html_reporter import generate_report

def main():
    tests = load_tests("tests/test_cases.json")
    results = run_tests(tests)
    generate_report(results)

if __name__ == "__main__":
    main()