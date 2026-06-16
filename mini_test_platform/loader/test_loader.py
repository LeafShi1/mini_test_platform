# loader/test_loader.py
import json

def load_tests(path):
  # Open the file with readonly and load the json content,
  # release the file handle and return the content
    with open(path, "r") as f:
        return json.load(f)