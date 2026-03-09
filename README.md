# OpenSoar & XCSoar Data Pipeline for Airspaces and Waypoints

In a nutshell: run this once a year and you'll be up to date with all COMBINED European airspaces from OpenAIP, all waypoints, VFR reporting points, and obstacles.

[OpenSoar](https://github.com/OpenSoarGroup/OpenSoar) and [XCSoar](https://www.xcsoar.org/) are tactical glide computers for Android/Linux.

You can download OpenSoar via this link: [https://www.opensoar.de/releases/](https://www.opensoar.de/releases/) - download the newest release version (7.43 or higher). This is preferred over XCSoar (as of March 2026) as it is actively maintained and has some nice features like SkySight integration. You are free to use the classic XCSoar, but you might encounter some difficulties while installing this content.

This repository provides a fully automated workflow for glider pilots to manage flight data. It bridges the gap between official OpenAIP data (airspaces, obstacles, waypoints) and your own custom flight computer configurations. Everything is compiled into a single, organized directory (`final-folder`) ready to be loaded directly onto your flight computer.

## Credits

* **Philip ([cumulophib](https://github.com/cumulophib)):** Created the project, OpenAIP integration, custom data merging, and automated packaging scripts.

---

## Project Structure

The project is organized to separate automated downloads from your personal, hand-made files:

* **`nav-airspaces/`**: The core for navigation data.
    * `input/`: **Your custom files.** Put custom airspaces (e.g., `loxn_loat_asp.txt`), waypoints, or obstacle files into the relevant subfolders.
    * `openaip_downloads/`: Temporary folder where automated cloud files are stored.
    * `output/`: Where the script generates the merged master files from OpenAIP only.
* **`final-folder/`**: Copy the contents of this folder to your OpenSoar/XCSoar directory and you're good to go!

---

## Running the Code (Building your Files)

You need Python 3 installed to run this pipeline.

First, set up a virtual environment in the root folder. You can do this by navigating to this root folder in your terminal (for example, in Visual Studio Code) and copying these commands:

```bash
python3 -m venv venv
```

Activate it:

```bash
# On Mac/Linux:
source venv/bin/activate

# On Windows (Note: The code may require modifications to run on Windows):
call venv\scripts\activate.bat
```

Install the necessary dependencies:

```bash
python3 -m pip install -Ur requirements.txt
```

### The 2-Step Build Workflow

To prepare your flight data, run these commands in order from the root directory:

**1. Update Airspaces, Waypoints & Obstacles**
Fetches the latest European legacy V1 data from OpenAIP, deep-cleans it, and merges it with your personal files in the `input` folders.
```bash
python3 nav-airspaces/openaip_api.py
```

**2. Create the Final Package**
Gathers the OpenAIP results and builds the ready-to-use `final-folder`. Make sure you have also added any custom waypoints or airspaces in the `input` folder if you want them to be merged with all the other data.
```bash
python3 build_final.py
```

---

## Installation on Device

Once `build_final.py` finishes, follow these steps to load the data onto your flight computer:

1. **Copy to Device:** Copy the entire contents of `final-folder` (all `.cup` and `.txt` files) into the app's data directory on your Android device. Note that you must copy the *contents* of the folder, not the `final-folder` itself.
    * **Standard Android (OpenSoar):** `Android/media/de.opensoar` (Note: This folder in `media` only exists when you have installed the NEWEST OpenSoar release from their website.)
    * **Older versions or XCSoar:** `Android/media/org.xcsoar` (Note: This is the location where older OpenSoar versions or XCSoar expect the files to be. This can be tricky on newer Android versions, since they restrict access to the data folder.)
2. **Configure the App:** Open XCSoar/OpenSoar and go to **Config > System > Site Files**. Set the following:
    * **Waypoints:** `combined_airports_navaids.cup`
    * **More Waypoints:** `combined_obstacles.cup`
    * **Airspaces:** `combined_airspaces.txt`
    * **FLARM / OGN Details:** Download and select your `.fln` file.
3. **Restart the app!**

---

## Contributing & Support

* **Code Contributions - Philip Heinrich (cumulophib):** Contributions to this codebase are welcome. Visit Philip's website to buy amazing gliding and aviation wall art at:
**[www.cumulophib.com](https://www.cumulophib.com)**
Follow Philip's gliding adventures on YouTube:
**[www.youtube.com/@cumulophib](https://www.youtube.com/@cumulophib)**

---

**IMPORTANT DISCLAIMER:** This software only automates the downloading and merging of data. We do not guarantee the accuracy or correctness of any information, especially regarding airspaces and navigation data. Additionally, it is possible that downloads may become corrupted, potentially leading to missing airspace information. While we have never encountered such a situation, it remains a possibility. You, as the pilot in command, are solely responsible for cross-checking and verifying your flight data before takeoff!
