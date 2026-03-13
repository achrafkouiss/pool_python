import sys
import os
import site


def check_virtualenv():
    # sys.prefix is the venv, sys.base_prefix is the system Python
    return sys.prefix != sys.base_prefix

if check_virtualenv():
    env_path = sys.prefix
    env_name = os.path.basename(env_path)
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(site.getsitepackages()[0])


else:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {os.path.realpath(sys.executable)}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows\n")

    print("Then run this program again")
# sys.prefix gives the root path of the current Python interpreter

# The name is often the last part of the path
# print(env_name)
