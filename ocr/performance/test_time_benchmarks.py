import importlib
import numpy as np
import pytest

# (name, input‐shape, default‐params)
SCRIPTS = [
    ("grayscale",       (1000, 1000, 3), {}),
    ("hist_equalization",(1000, 1000, 3), {}),
    ("threshold",       (1000, 1000),    {"method": "otsu", "threshold_value": 0}),
    ("resize",          (1000, 1000, 3), {"target_width": 800, "target_height": 600, "upscale_only": False}),
    # …add others here…
]

@pytest.mark.parametrize("name,shape,params", SCRIPTS)
def test_time_benchmark(benchmark, name, shape, params):
    """
    Benchmark preprocess(<random image>, params) for each script.
    """
    module = importlib.import_module(f"preprocessing_image.scripts.{name}")
    img = np.random.randint(0, 256, size=shape, dtype=np.uint8)
    # benchmark will call module.preprocess(img, params) many times
    benchmark(module.preprocess, img, params)
