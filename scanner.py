import subprocess
import json

import subprocess
import json

def scan_python(requirements_path):
    result = subprocess.run(
        ["safety", "check", "-r", requirements_path, "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("\n=== SAFETY STDOUT ===")
    print(result.stdout)
    print("\n=== SAFETY STDERR ===")
    print(result.stderr)
    print("\n=== SAFETY RETURN CODE ===")
    print(result.returncode)

    if result.returncode != 0:
        return {"error": result.stderr}

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as e:
        return {"error": "Invalid JSON from safety output.", "raw": result.stdout}


def scan_node(path):
    subprocess.run(["npm", "install"], cwd=path)
    result = subprocess.run(
        ["npm", "audit", "--json"],
        capture_output=True, text=True, cwd=path
    )
    print("SAFETY STDOUT:", result.stdout)
    print("SAFETY STDERR:", result.stderr)
    return json.loads(result.stdout)

