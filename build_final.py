"""
OpenSoar / XCSoar Final Packager
=======================
1. Clears 'final-folder' for a clean build.
2. Copies the deep-cleaned OpenAIP master files (airspaces, navaids, obstacles).
"""

import os
import shutil

# --- Configuration & Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NAV_OUTPUT_DIR = os.path.join(BASE_DIR, 'nav-airspaces', 'output')
FINAL_DIR = os.path.join(BASE_DIR, 'final-folder')


def clear_final_folder():
    """Wipes the final folder to ensure no old/broken files remain."""
    if os.path.exists(FINAL_DIR):
        print("Cleaning 'final-folder' for a fresh build...")
        try:
            shutil.rmtree(FINAL_DIR)
        except Exception as e:
            print(f"Could not fully wipe folder: {e}")
    os.makedirs(FINAL_DIR, exist_ok=True)


def copy_nav_files():
    """Copies the master airspaces, navaids and obstacles."""
    print("\n--- Copying OpenAIP Master Files ---")
    if not os.path.exists(NAV_OUTPUT_DIR):
        print("Error: nav-airspaces/output not found!")
        return
    for filename in os.listdir(NAV_OUTPUT_DIR):
        src_path = os.path.join(NAV_OUTPUT_DIR, filename)
        if os.path.isfile(src_path):
            print(f"  Including: {filename}")
            shutil.copy2(src_path, FINAL_DIR)


def main():
    clear_final_folder()
    copy_nav_files()
    print(f"\nALL DONE! Copy the contents of {FINAL_DIR} to your device.")


if __name__ == "__main__":
    main()
