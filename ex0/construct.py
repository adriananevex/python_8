import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        for path in site.getsitepackages():
            print(path)
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")

        print("\nThen run this program again.")
