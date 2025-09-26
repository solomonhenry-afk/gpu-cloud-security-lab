#!/usr/bin/env python3
try:
    import pynvml
except Exception:
    print("pynvml not installed. Install: pip install nvidia-ml-py3")
    exit(0)

pynvml.nvmlInit()
count = pynvml.nvmlDeviceGetCount()
print(f"CUDA devices available: {count}")
for i in range(count):
    h = pynvml.nvmlDeviceGetHandleByIndex(i)
    name = pynvml.nvmlDeviceGetName(h).decode()
    mem = pynvml.nvmlDeviceGetMemoryInfo(h)
    print(f"GPU {i}: {name} / total {mem.total//(1024**2)} MB free {mem.free//(1024**2)} MB")
pynvml.nvmlShutdown()
