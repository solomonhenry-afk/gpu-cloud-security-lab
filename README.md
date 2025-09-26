GPU Cloud Security Lab (2025)

This project simulates GPU-enabled workloads in Kubernetes and demonstrates container isolation, CIS compliance checks, GPU (CUDA) memory hygiene research, and Kubernetes hardening automation.  

It is designed as a defensive portfolio project to show how modern enterprises can secure GPU-first cloud environments (like Runpod, AWS, or GCP).

Quickstart
1. Deploy manifests: `kubectl apply -f k8s/`
2. Run local checks: `python3 tools/k8s_hardening_check.py`
3. Inspect GPU devices: `python3 cuda-research/cuda-memory-check.py`
