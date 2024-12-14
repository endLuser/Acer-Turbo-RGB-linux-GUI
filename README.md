

# Unofficial Acer Gaming RGB Keyboard Backlight and Turbo Mode Linux Kernel Module GUI
_For Acer Predator, Acer Helios, Acer Nitro_

<!-- ![Acer Gaming Keyboard](keyboard.webp) -->

[![Good First Issues](https://img.shields.io/github/issues/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/good%20first%20issue?style=flat&logo=github&logoColor=green&label=Good%20First%20issues)](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)
[![Help Wanted Issues](https://img.shields.io/github/issues/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/help%20wanted?style=flat&logo=github&logoColor=b545d1&label=%22Help%20Wanted%22%20issues)](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) 
[![Help Wanted PRs](https://img.shields.io/github/issues-pr/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/help%20wanted?style=flat&logo=github&logoColor=b545d1&label=%22Help%20Wanted%22%20PRs)](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/pulls?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) 
[![GitHub Issues](https://img.shields.io/github/issues/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module?style=flat&logo=github&logoColor=red&label=Issues)](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/issues?q=is%3Aopen)

[![Discord Server](https://dcbadge.vercel.app/api/server/bNa4Qw8rPH)](https://discord.gg/ybWvSRfSY5)

--- 

### Description

This project extends the `acer-wmi` Linux kernel module to support Acer gaming functions, including **Turbo Mode** and **RGB keyboard backlighting** for various Acer laptops such as Predator, Helios, and Nitro series. Inspired by the [faustus (for ASUS)](https://github.com/hackbnw/faustus) project, it reverse-engineers the official Predator Sense app to interact with low-level WMI methods.

**Warning:**  
This module is developed **without official support** from Acer and is based on reverse-engineering. As such, it may not be compatible with all Acer models. Use at your own risk.

---

### Compatibility Table

| Product Name     | Turbo Mode (Implemented) | Turbo Mode (Tested)  | RGB (Implemented) | RGB (Tested)  |
|------------------|--------------------------|----------------------|-------------------|---------------|
| AN515-45         | No                       | No                   | Yes               | Yes           |
| AN515-55         | No                       | No                   | Yes               | Yes           |
| PH315-52         | Yes                      | Yes                  | Yes               | Yes           |
| PH315-53         | Yes                      | Yes                  | Yes               | Yes           |
| PH317-53         | Yes                      | Yes                  | Yes               | Yes           |
| PH517-51         | Yes                      | No                   | Yes               | No            |
| PT515-51         | Yes                      | Yes                  | Yes               | Yes           |
| PH717-71         | Yes                      | No                   | Yes               | No            |
| PH717-72         | Yes                      | No                   | Yes               | No            |

_If your model is not listed, please check the [GitHub Issues page](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/issues) and report your findings._

---

### Requirements

1. **Linux headers**: Ensure you have the Linux headers installed.
   - **Ubuntu/Debian**:  
     ```bash
     sudo apt-get install linux-headers-$(uname -r) gcc make
     ```
   - **Arch Linux**:  
     ```bash
     sudo pacman -S linux-headers
     ```

2. **Secure Boot**: If you have Secure Boot enabled and encounter errors like `Key was rejected by service`, you'll need to sign the module yourself. [Follow this guide](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/issues/28#issuecomment-1054423776) to resolve it.

3. **Rsync**: You’ll need `rsync` to install the module properly:
   ```bash
   rsync --version
   ```
4.  **PyQt5**:
    ```
    pip3 install PyQt5
    ```

---

### Installation

#### One-Time Installation (Will not survive reboot)
```bash
git clone https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
cd acer-predator-turbo-and-rgb-keyboard-linux-module
chmod +x ./*.sh
sudo ./install.sh
```

#### Persistent Installation (Systemd/OpenRC service)

##### Arch Linux (from ExodiaOS Repo)
```bash
sudo pacman -U Predator-Sense-CLI-{version}-any.pkg.tar.zst
```

##### Systemd (Works after reboot)
```bash
git clone https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
cd acer-predator-turbo-and-rgb-keyboard-linux-module
chmod +x ./*.sh
sudo ./install_service.sh
```

##### OpenRC (Works after reboot)
```bash
git clone https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
cd acer-predator-turbo-and-rgb-keyboard-linux-module
chmod +x ./*.sh
sudo ./install_openrc.sh
```
### To use just run GUI.py file

---
<details>
  <summary>
  Click to reveal CLI Usage Instructions
  </summary>

### Usage

- **Turbo Mode**: Should be activated by using the turbo button on your keyboard.
  
- **RGB Keyboard**:  
  The module will create a new character device at `/dev/acer-gkbbl-0` for communication. Use the provided Python scripts to control RGB effects.

#### `keyboard.py` - Basic Script for RGB Control

Run the script using:
```bash
python keyboard.py
```

#### `facer_rgb.py` - Advanced Script for RGB Control

This script offers more advanced control over your keyboard's RGB settings. You can modify effects, brightness, colors, speed, and more.

For help, run:
```bash
./facer_rgb.py --help
```

**Sample usage**:

- **Breath effect with purple color** (speed=4, brightness=100):  
  ```bash
  ./facer_rgb.py -m 1 -s 4 -b 100 -cR 255 -cG 0 -cB 255
  ```

- **Neon effect** (speed=3, brightness=100):  
  ```bash
  ./facer_rgb.py -m 2 -s 3 -b 100
  ```

- **Wave effect** (speed=5, brightness=100):  
  ```bash
  ./facer_rgb.py -m 3 -s 5 -b 100
  ```

- **Shifting effect with blue color** (speed=5, brightness=100):  
  ```bash
  ./facer_rgb.py -m 4 -s 5 -b 100 -cR 0 -cB 255 -cG 0
  ```

- **Zoom effect with green color** (speed=7, brightness=100):  
  ```bash
  ./facer_rgb.py -m 5 -s 7 -b 100 -cR 0 -cB 0 -cG 255
  ```

For static coloring in specific zones, use:
```bash
./facer_rgb.py -m 0 -z 1 -cR 0 -cB 255 -cG 0
```
</details>

---

### Known Issues

- If installation fails, check the [installation issue](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/issues/4#issuecomment-905486393).
- Rebooting or booting into Windows and using Predator Sense may reset ACPI registers, helping resolve any issues.

---

### Uninstallation

To uninstall the module, run:
```bash
./uninstall.sh
```

If installed as a service, use:
```bash
./uninstall_service.sh
```

#### For Arch Linux (AUR)
To uninstall from the AUR:
```bash
sudo pacman -R Predator-Sense-systemd-git
```

---

### Contributions

This project would not be possible without the amazing contributions from the community. To see a full list of contributors, visit the [contributors page](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/graphs

/contributors).

If you'd like to help, please see the [contribution guidelines](CONTRIBUTING.md) and [open an issue](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/issues).

---

### License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

### Links

- [Project Page on GitHub](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module)
- [Discussion and Support via Discord (only for script)](https://discord.gg/ybWvSRfSY5) 

---

