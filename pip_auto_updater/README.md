# 🛠️ Pip Auto-Updater

This script automates the process of updating all outdated Python packages installed via `pip`. It’s designed for developers and QA engineers who want to maintain clean, up-to-date environments with minimal manual effort.

## Features

- Identifies all outdated packages using `pip list --outdated` excluding built-ins.
- Iteratively upgrades each package via `pip install --upgrade`, ensuring minimal disruption.
---

## Usage

### Run the script directly:
```bash
python pip_auto_updater/update_packages.py 
```

## Compatibility
- Python 3.8+
- Pip 21+

## Notes
- Some packages may fail to update due to system-level constraints or dependency conflicts.
- It’s recommended to run this inside a virtual environment to avoid breaking global installs.

## Author
Ayush Srivastava