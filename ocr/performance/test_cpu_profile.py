import cProfile
import io
import importlib
import numpy as np
import pstats
import pytest

@pytest.mark.parametrize("name,shape,params", [
    ("resize", (2000, 2000, 3), {"target_width": 800, "target_height": 600, "upscale_only": False}),
])
def test_cpu_profile(name, shape, params):
    """
    Run cProfile on one call and write the top‐10 cumulative hotspots to logs/<name>_cprofile.txt
    """
    # Dynamically import the module based on the 'name' argument
    module = importlib.import_module(f"preprocessing_image.scripts.{name}")

    # Generate random image data with the given shape
    img = np.random.randint(0, 256, size=shape, dtype=np.uint8)

    # Create and enable a cProfile instance to track the function call
    pr = cProfile.Profile()
    pr.enable()

    # Run the actual function
    module.preprocess(img, params)

    # Disable profiling after the function call
    pr.disable()

    # Output the profiling data to a string for further analysis
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats(10)

    # Write profiling data to the log file for inspection
    with open(f"logs/{name}_cprofile.txt", "w") as f:
        f.write(s.getvalue())

    # Always pass the test for profiling purposes
    assert True
