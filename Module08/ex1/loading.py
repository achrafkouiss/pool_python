import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import importlib
from importlib.metadata import PackageNotFoundError

required_packages = {
    'pandas': "Data manipulation ready",
    'requests': "Network access ready",
    'matplotlib': "Visualization ready"

}

print("\nLOADING STATUS: Loading programs...\n")

print("Checking dependencies:")
def is_installed(module_name, msg):
    version = importlib.metadata.version(module_name)
    print(f"[OK] {module_name} ({version}) - {msg}")

for package_name, value in required_packages.items():
    try:
        is_installed(package_name, value)
    except PackageNotFoundError:
        print(f"* **{package_name}**: Not Found (Package not installed)")
    except Exception as e:
        print(f"* **{package_name}**: Not Found (Package not installed)")


print("Analyzing Matrix data...")
print("Processing 1000 data points...")

data = np.random.randn(1000)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",data)
print("Generating visualization...\n")
df = pd.DataFrame(data).cumsum()
plt.plot(df)
plt.savefig("matrix_analysis.png")

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")