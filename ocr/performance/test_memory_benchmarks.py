import importlib
import numpy as np
import pytest
from memory_profiler import memory_usage

# Define the scripts to test
SCRIPTS = [
    ("grayscale", (2000, 2000, 3), {}),
    ("resize",    (2000, 2000, 3), {"target_width": 800, "target_height": 600, "upscale_only": False}),
    # Add more operations here (e.g., "deskew", "threshold", etc.)
]

@pytest.mark.parametrize("name,shape,params", SCRIPTS)
def test_memory_usage(name, shape, params):
    """
    Measure peak memory (RSS) for one call of preprocess().
    This test measures memory usage during a single preprocess operation,
    ensuring that it stays within a reasonable limit.
    """
    module = importlib.import_module(f"preprocessing_image.scripts.{name}")  # Dynamically load the module
    img = np.random.randint(0, 256, size=shape, dtype=np.uint8)  # Generate a random image

    # Memory usage measurement using memory_profiler
    # `memory_usage` returns a list of memory usage values during the execution
    mem = memory_usage((module.preprocess, (img, params)), max_iterations=1, retval=False)

    # Calculate peak memory usage (in MiB)
    peak_mb = max(mem) - min(mem)

    # Log the peak memory usage for each test case
    print(f"{name}: peak ΔRAM = {peak_mb:.2f} MiB")

    # Optionally enforce a threshold for memory usage (this can be adjusted as needed)
    assert peak_mb < 200.0  # Set a sensible upper bound based on your system's capabilities

