

# Unofficial Acer Gaming RGB Keyboard Backlight and Turbo Mode Linux Kernel Module GUI
_For Acer Predator, Acer Helios, Acer Nitro_

--- 

### Description
( This is a work in progress software)
This project extends the `acer-predator-turbo-and-rgb-keyboard-linux-module` to Provide GUI functions, including **Turbo Mode** and **RGB keyboard backlighting** for various Acer laptops such as Predator, Helios, and Nitro series.

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

### License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

### Links

- [Project Page on GitHub](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module)

---

