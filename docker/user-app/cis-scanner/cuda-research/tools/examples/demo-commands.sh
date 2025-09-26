#!/usr/bin/env bash
# Demo commands to run locally
kubectl apply -f k8s/namespace-isolation.yaml
kubectl apply -f k8s/gpu-workload-deployment.yaml
python3 tools/k8s_hardening_check.py
python3 cis-scanner/cis_docker_check.py
