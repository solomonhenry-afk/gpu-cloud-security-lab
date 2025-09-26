#!/usr/bin/env python3
from pathlib import Path
def check_dockerfile(path="docker/Dockerfile.gpu"):
    issues=[]
    text=Path(path).read_text() if Path(path).exists() else ""
    if "USER root" in text or "useradd" not in text:
        issues.append("May run as root or no non-root user found")
    if "ssh" in text.lower():
        issues.append("SSH present in container")
    return issues

if __name__ == "__main__":
    for i in check_dockerfile():
        print("WARN:", i)
    print("CIS checks complete.")
