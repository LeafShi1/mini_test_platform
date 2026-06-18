# main.py
import sys

from logging import config

from config.config_loader import load_config
from loader.test_loader import load_tests
from runner.test_runner import run_tests
from reporter.html_reporter import generate_report

def main():

    config_file = (
        sys.argv[1]
        if len(sys.argv)>1
        else "config.yaml"
      )

    config=load_config(config_file)
    test_case_path = config["test_case_path"]
    output_file = (
        f"{config['report']['output_dir']}/"
        f"{config['report']['report_name']}"
      )

    tests = load_tests(test_case_path)
    results = run_tests(tests)
    generate_report(results, output_file)

if __name__ == "__main__":
    main()