import json
def load_tests(path):
  with open(path, "r") as f:
    return json.load(f)



