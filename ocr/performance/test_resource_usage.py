import importlib
import time
import numpy as np
import psutil
import pytest

@pytest.mark.parametrize("name,shape,params", [
    ("resize", (2000, 2000, 3), {"target_width": 800, "target_height": 600, "upscale_only": False}),
])
def test_resource_usage(name, shape, params):
    """
    Measure wall‐clock, user‐CPU, system‐CPU, and ΔRSS for one call.
    """
    module = importlib.import_module(f"preprocessing_image.scripts.{name}")
    img = np.random.randint(0, 256, size=shape, dtype=np.uint8)
    proc = psutil.Process()

    mem_before = proc.memory_info().rss
    cpu_before = proc.cpu_times()
    t0 = time.time()

    module.preprocess(img, params)

    t1 = time.time()
    cpu_after = proc.cpu_times()
    mem_after = proc.memory_info().rss

    wall = t1 - t0
    user_cpu = cpu_after.user - cpu_before.user
    sys_cpu  = cpu_after.system - cpu_before.system
    rss_diff = (mem_after - mem_before) / (1024**2)

    print(f"{name}: wall={wall:.3f}s, user={user_cpu:.3f}s, sys={sys_cpu:.3f}s, ΔRSS={rss_diff:.2f}MiB")

    # no hard asserts—just surface the numbers for review
    assert wall < 1.0  # or adjust to acceptable latency
