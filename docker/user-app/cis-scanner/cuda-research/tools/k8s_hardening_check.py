#!/usr/bin/env python3
import yaml, sys
def scan(file_path):
    with open(file_path) as f:
        docs = list(yaml.safe_load_all(f))
    for d in docs:
        spec = d.get("spec",{})
        template = spec.get("template",{})
        pod_spec = template.get("spec", spec.get("spec", {}))
        if 'hostNetwork' in pod_spec and pod_spec.get('hostNetwork'):
            print("WARN: hostNetwork found")
        for c in pod_spec.get("containers",[]):
            sc = c.get("securityContext",{})
            if sc.get("privileged"):
                print(f"WARN: container {c.get('name')} is privileged")
            if sc.get("runAsUser") in (0, None):
                print(f"WARN: container {c.get('name')} might run as root")
if __name__ == "__main__":
    target="k8s/gpu-workload-deployment.yaml"
    try:
        scan(target)
    except FileNotFoundError:
        print(f"Target manifest not found: {target}")
