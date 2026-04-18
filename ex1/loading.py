import sys
import importlib


def check_dependencies(packages):
    modules = {}
    missing = []

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for package in packages:
        try:
            module = importlib.import_module(package)
            modules[package] = module

            version = getattr(module, "__version__", "unknown")

            if package == "pandas":
                print(f"[OK] pandas ({version}) - Data manipulation ready")
            elif package == "numpy":
                print(f"[OK] numpy ({version}) - Numerical computation ready")
            elif package == "matplotlib":
                print(f"[OK] matplotlib ({version}) - Visualization ready")
            elif package == "requests":
                print(f"[OK] requests ({version}) - Network access ready")

        except ImportError:
            print(f"[MISSING] {package} - Not installed")
            missing.append(package)

    return modules, missing


def main():
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    modules, missing = check_dependencies(packages)

    if missing:
        print("\nMissing dependencies detected.")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("\nOr with Poetry:")
        print("poetry install")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")

    np = modules["numpy"]
    pd = modules["pandas"]
    plt = importlib.import_module("matplotlib.pyplot")

    data = np.random.normal(0, 1, 1000)

    df = pd.DataFrame({"signal": data})
    df["rolling_mean"] = df["signal"].rolling(window=20).mean()

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    plt.figure()
    plt.plot(df["signal"])
    plt.plot(df["rolling_mean"])
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
