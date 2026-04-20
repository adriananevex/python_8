import sys
import importlib
from importlib import metadata


def get_version(package):
    try:
        return metadata.version(package)
    except metadata.PackageNotFoundError:
        return "unknown"


def check_dependencies(packages):
    modules = {}
    missing = []

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:\n")

    for package in packages:
        try:
            module = importlib.import_module(package)
            modules[package] = module

            version = get_version(package)

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


def show_pip_vs_poetry():
    print("\n=== PIP vs POETRY DIFFERENCES ===\n")

    print(" PIP (traditional way):")
    print("- Installs packages manually")
    print("- Uses requirements.txt")
    print("- No project management")
    print("- You manage virtual environments manually (venv)")
    print("- Install command: pip install -r requirements.txt")
    print("- Run: python loading.py\n")

    print(" POETRY (modern way):")
    print("- Manages dependencies + project together")
    print("- Uses pyproject.toml")
    print("- Automatically creates virtual environments")
    print("- Handles dependency resolution better")
    print("- Install command: poetry install")
    print("- Run: poetry run python loading.py\n")


def show_versions(modules):
    print("\nInstalled package versions:\n")

    for name in modules:
        version = get_version(name)
        print(f"- {name}: {version}")


def main():
    packages = ["pandas", "numpy", "matplotlib", "requests"]

    modules, missing = check_dependencies(packages)

    if missing:
        print("\nMissing dependencies detected.\n")

        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("python3 loading.py")

        print("\nInstall with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")

        sys.exit(1)

    show_pip_vs_poetry()
    show_versions(modules)

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
    plt.plot(df["signal"], label="signal")
    plt.plot(df["rolling_mean"], label="rolling mean")
    plt.legend()

    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
