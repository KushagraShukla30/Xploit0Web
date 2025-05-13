import subprocess
import json

def scan_python(req_file):
    result = subprocess.run(
        ["safety", "check", "-r", req_file, "--json"],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)

def scan_node(path):
    subprocess.run(["npm", "install"], cwd=path)
    result = subprocess.run(
        ["npm", "audit", "--json"],
        capture_output=True, text=True, cwd=path
    )
    return json.loads(result.stdout)
