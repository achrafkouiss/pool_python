import sys
from importlib.metadata import version, PackageNotFoundError

# Packages required by the program and a short description
required_packages = {
    "pandas": "Data manipulation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}

print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")

# List that will store any missing packages
missing = []


# Check whether a package is installed and retrieve its version
def check_package(name: str, msg: str) -> None:
    try:
        # Retrieve installed package version using importlib.metadata
        pkg_version = version(name)

        # Package found
        print(f"[OK] {name} ({pkg_version}) - {msg}")

    except PackageNotFoundError:
        # Package is not installed
        print(f"[MISSING] {name} - Package not installed")
        missing.append(name)

    except Exception:
        # Catch unexpected metadata errors (rare but possible)
        print(f"[ERROR] {name} - Could not determine version")
        missing.append(name)


# Iterate through all required packages and check each one
for pkg, msg in required_packages.items():
    check_package(pkg, msg)


# If some packages are missing, show install instructions and exit
if missing:
    print("\nMissing dependencies detected.")
    print("Install them using one of the following:\n")
    print("pip install -r requirements.txt")
    print("or")
    print("poetry install\n")
    sys.exit(1)


# Safe imports (done only after verifying packages exist)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print("\nAnalyzing Matrix data...")
print("Processing 1000 data points...")


# Generate 1000 random values from a normal distribution
data = np.random.randn(1000)


print("Generating visualization...\n")


# Convert the data into a DataFrame and compute cumulative sum
df = pd.DataFrame(data).cumsum()

# Plot the cumulative data
plt.plot(df)

# Save the generated figure to a file
plt.savefig("matrix_analysis.png")


print("Analysis complete!")
print("Results saved to: matrix_analysis.png")