import sys
import importlib


if __name__ == "__main__":
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    modules = {}

    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    for package in packages:
        try:
            module = importlib.import_module(package)
            modules[package] = module
            if module.__name__ == "pandas":
                print(f"[OK] {module.__name__} ({module.__version__}) \
                      - Data manipulation ready")
            elif module.__name__ == "requests":
                print(f"[OK] {module.__name__} ({module.__version__}) \
                      - Network access ready")
            elif module.__name__ == "matplotlib":
                print(f"[OK] {module.__name__} ({module.__version__}) \
                      - Visualization ready")
        except ImportError:
            print(f"[MISSING] {package} - Not installed")

    print("\nAnalyzing Matrix data...")

    data = modules["numpy"].random.normal(0, 1, 1000)
    df = modules["pandas"].DataFrame({"signal": data})
    df["rolling_mean"] = df["signal"].rolling(window=20).mean()

    plt = importlib.import_module("matplotlib.pyplot")

    plt.plot(df["signal"])
    plt.plot(df["rolling_mean"])

    plt.savefig(f"{sys.prefix}/matrix_analysis.png")

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
