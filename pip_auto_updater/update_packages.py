import subprocess
import sys

def update_outdated_packages():
    """
    Updates all outdated third-party Python packages using pip.
    Built-in and system packages are excluded.
    """
    try:
        # Get list of outdated packages
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--outdated", "--format=json"],
            capture_output=True, text=True, check=True
        )
        outdated = eval(result.stdout)  # JSON parsing without import for simplicity

        if not outdated:
            print("All packages are up to date.")
            return

        print(f"Found {len(outdated)} outdated packages. Updating...\n")

        for pkg in outdated:
            name = pkg['name']
            current_version = pkg['version']
            latest_version = pkg['latest_version']
            print(f"Updating {name} ({current_version} → {latest_version})...")

            try:
                subprocess.run(
                    [sys.executable, "-m", "pip", "install", "--upgrade", name],
                    check=True
                )
                print(f"✅ {name} updated successfully.\n")
            except subprocess.CalledProcessError:
                print(f"Failed to update {name}. Skipping...\n")

    except Exception as e:
        print(f"Error occurred: {e}")

update_outdated_packages()