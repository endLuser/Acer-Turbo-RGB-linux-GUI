import sys
import json
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QSlider, QPushButton, QTabWidget, QColorDialog, QLineEdit, QFileDialog # type: ignore
from PyQt5.QtCore import Qt # type: ignore
from PyQt5.QtGui import QColor, QFont # type: ignore

class RGBControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acer RGB Control")
        self.setGeometry(100, 100, 500, 400)

        self.mode_options = ["Static", "Breath", "Neon", "Wave", "Shifting", "Zoom"]
        self.zone_options = [1, 2, 3, 4]

        self.selected_color = QColor(255, 255, 255)  # Default to white

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Title Label
        self.title_label = QLabel("RGB Lighting Control")
        self.title_label.setFont(QFont("Roboto", 18, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #6200EE;")
        layout.addWidget(self.title_label)

        # Tabs for Modes
        self.tabs = QTabWidget(self)
        self.create_tabs()
        layout.addWidget(self.tabs)

        # Save Profile Section
        self.profile_name_input = QLineEdit(self)
        self.profile_name_input.setPlaceholderText("Enter profile name")
        self.profile_name_input.setStyleSheet("border: 1px solid #6200EE; border-radius: 4px; padding: 8px;")
        
        self.save_profile_button = QPushButton("Save Profile", self)
        self.save_profile_button.clicked.connect(self.save_profile)
        self.save_profile_button.setStyleSheet(self.button_style())

        # Load Profile Section
        self.load_profile_button = QPushButton("Load Profile", self)
        self.load_profile_button.clicked.connect(self.load_profile)
        self.load_profile_button.setStyleSheet(self.button_style())

        # List profiles dropdown
        self.profile_list = QComboBox(self)
        self.profile_list.addItems(self.list_profiles())  # Populate with available profiles

        # Apply button to run the configuration
        self.run_button = QPushButton("Apply Settings")
        self.run_button.setFont(QFont("Roboto", 12))
        self.run_button.setStyleSheet(self.button_style())
        self.run_button.clicked.connect(self.run_command)

        layout.addWidget(self.run_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.profile_name_input)
        layout.addWidget(self.save_profile_button)
        layout.addWidget(self.load_profile_button)
        layout.addWidget(self.profile_list)

        # Set the layout
        self.setLayout(layout)
        self.setStyleSheet("background-color: #F5F5F5; color: #000000;")

    def button_style(self):
        return """
        background-color: #6200EE;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        font-size: 14px;
        margin: 5px 0;
        """

    def create_tabs(self):
        # Static Tab
        static_tab = QWidget()
        static_layout = QVBoxLayout()
        self.static_mode_controls(static_layout)
        static_tab.setLayout(static_layout)

        # Breath Tab
        breath_tab = QWidget()
        breath_layout = QVBoxLayout()
        self.breath_mode_controls(breath_layout)
        breath_tab.setLayout(breath_layout)

        # Neon Tab
        neon_tab = QWidget()
        neon_layout = QVBoxLayout()
        self.neon_mode_controls(neon_layout)
        neon_tab.setLayout(neon_layout)

        # Wave Tab
        wave_tab = QWidget()
        wave_layout = QVBoxLayout()
        self.wave_mode_controls(wave_layout)
        wave_tab.setLayout(wave_layout)

        # Shifting Tab
        shifting_tab = QWidget()
        shifting_layout = QVBoxLayout()
        self.shifting_mode_controls(shifting_layout)
        shifting_tab.setLayout(shifting_layout)

        # Zoom Tab
        zoom_tab = QWidget()
        zoom_layout = QVBoxLayout()
        self.zoom_mode_controls(zoom_layout)
        zoom_tab.setLayout(zoom_layout)

        # Add tabs
        self.tabs.addTab(static_tab, "Static")
        self.tabs.addTab(breath_tab, "Breath")
        self.tabs.addTab(neon_tab, "Neon")
        self.tabs.addTab(wave_tab, "Wave")
        self.tabs.addTab(shifting_tab, "Shifting")
        self.tabs.addTab(zoom_tab, "Zoom")

    def static_mode_controls(self, layout):
        layout.addWidget(QLabel("Color"))
        self.color_button = QPushButton('Choose Color')
        self.color_button.clicked.connect(self.open_color_picker)
        self.color_button.setStyleSheet(self.button_style())
        layout.addWidget(self.color_button)

        layout.addWidget(QLabel("Zone"))
        self.zone_combobox = QComboBox()
        self.zone_combobox.addItems([str(i) for i in self.zone_options])
        layout.addWidget(self.zone_combobox)

    def breath_mode_controls(self, layout):
        layout.addWidget(QLabel("Color"))
        self.color_button = QPushButton('Choose Color')
        self.color_button.clicked.connect(self.open_color_picker)
        self.color_button.setStyleSheet(self.button_style())
        layout.addWidget(self.color_button)

        layout.addWidget(QLabel("Speed"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 9)  # Speed range from 1 to 9
        self.speed_slider.setValue(4)  # Default to speed 4
        self.speed_label = QLabel(f"Speed: {self.speed_slider.value()}")
        self.speed_slider.valueChanged.connect(self.update_speed_label)  # Update label on change
        layout.addWidget(self.speed_slider)
        layout.addWidget(self.speed_label)

    def neon_mode_controls(self, layout):
        layout.addWidget(QLabel("Color"))
        self.color_button = QPushButton('Choose Color')
        self.color_button.clicked.connect(self.open_color_picker)
        self.color_button.setStyleSheet(self.button_style())
        layout.addWidget(self.color_button)

    def wave_mode_controls(self, layout):
        layout.addWidget(QLabel("Color"))
        self.color_button = QPushButton('Choose Color')
        self.color_button.clicked.connect(self.open_color_picker)
        self.color_button.setStyleSheet(self.button_style())
        layout.addWidget(self.color_button)

        layout.addWidget(QLabel("Speed"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 9)  # Speed range from 1 to 9
        self.speed_slider.setValue(4)  # Default to speed 4
        self.speed_label = QLabel(f"Speed: {self.speed_slider.value()}")
        self.speed_slider.valueChanged.connect(self.update_speed_label)  # Update label on change
        layout.addWidget(self.speed_slider)
        layout.addWidget(self.speed_label)

    def shifting_mode_controls(self, layout):
        layout.addWidget(QLabel("Color"))
        self.color_button = QPushButton('Choose Color')
        self.color_button.clicked.connect(self.open_color_picker)
        self.color_button.setStyleSheet(self.button_style())
        layout.addWidget(self.color_button)

        layout.addWidget(QLabel("Speed"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 9)  # Speed range from 1 to 9
        self.speed_slider.setValue(4)  # Default to speed 4
        self.speed_label = QLabel(f"Speed: {self.speed_slider.value()}")
        self.speed_slider.valueChanged.connect(self.update_speed_label)  # Update label on change
        layout.addWidget(self.speed_slider)
        layout.addWidget(self.speed_label)

    def zoom_mode_controls(self, layout):
        layout.addWidget(QLabel("Color"))
        self.color_button = QPushButton('Choose Color')
        self.color_button.clicked.connect(self.open_color_picker)
        self.color_button.setStyleSheet(self.button_style())
        layout.addWidget(self.color_button)

        layout.addWidget(QLabel("Speed"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 9)  # Speed range from 1 to 9
        self.speed_slider.setValue(4)  # Default to speed 4
        self.speed_label = QLabel(f"Speed: {self.speed_slider.value()}")
        self.speed_slider.valueChanged.connect(self.update_speed_label)  # Update label on change
        layout.addWidget(self.speed_slider)
        layout.addWidget(self.speed_label)

    def open_color_picker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_color = color
            self.color_button.setStyleSheet(f"background-color: {color.name()}; color: white; border-radius: 4px;")

    def update_speed_label(self):
        speed_value = self.speed_slider.value()
        self.speed_label.setText(f"Speed: {speed_value}")

    def save_profile(self):
        profile_name = self.profile_name_input.text().strip()
        if profile_name:
            self.save_profile_to_file(profile_name)

    def save_profile_to_file(self, profile_name):
        # Gather all settings to save
        profile_data = {
            "mode": self.tabs.currentIndex(),
            "color": self.selected_color.name(),  # Save the color as hex
            "speed": self.speed_slider.value(),
            "brightness": 100,  # Assuming fixed brightness for now
            "zone": self.zone_combobox.currentText() if self.tabs.currentIndex() == 0 else None
        }

        # Ensure the profiles directory exists
        profile_dir = os.path.join(os.path.expanduser("~"), ".config", "predator", "saved_profiles")
        os.makedirs(profile_dir, exist_ok=True)

        # Save the profile to a JSON file
        profile_path = os.path.join(profile_dir, f"{profile_name}.json")
        with open(profile_path, 'w') as profile_file:
            json.dump(profile_data, profile_file, indent=4)

        print(f"Profile saved as {profile_name}")

    def load_profile(self):
        profile_name = self.profile_list.currentText()
        if profile_name:
            self.load_profile_from_file(profile_name)

    def load_profile_from_file(self, profile_name):
        profile_dir = os.path.join(os.path.expanduser("~"), ".config", "predator", "saved_profiles")
        profile_path = os.path.join(profile_dir, f"{profile_name}.json")

        if os.path.isfile(profile_path):
            with open(profile_path, 'r') as profile_file:
                profile_data = json.load(profile_file)

            # Apply the settings from the profile
            self.tabs.setCurrentIndex(profile_data["mode"])
            self.selected_color = QColor(profile_data["color"])  # Set the color based on saved value
            self.set_color_display()

            self.speed_slider.setValue(profile_data["speed"])
            # Assuming brightness is fixed at 100 for simplicity
            print(f"Profile '{profile_name}' loaded successfully.")
        else:
            print(f"Profile '{profile_name}' not found.")

    def set_color_display(self):
        # Update color display based on selected color
        self.color_button.setStyleSheet(f"background-color: {self.selected_color.name()}; color: white; border-radius: 4px;")

    def list_profiles(self):
        profile_dir = os.path.join(os.path.expanduser("~"), ".config", "predator", "saved_profiles")
        profiles = []
        if os.path.isdir(profile_dir):
            profiles = [f[:-5] for f in os.listdir(profile_dir) if f.endswith(".json")]
        return profiles

    def run_command(self):
        mode = self.tabs.currentIndex()
        speed = self.speed_slider.value()
        brightness = 100  # Fixed for now
        red = self.selected_color.red()
        green = self.selected_color.green()
        blue = self.selected_color.blue()

        script_dir = os.path.dirname(os.path.realpath(__file__))
        script_path = os.path.join(script_dir, "facer_rgb.py")

        if not os.path.isfile(script_path):
            print(f"Error: {script_path} does not exist.")
            return

        command = ["python3", script_path, "-m", str(mode), "-s", str(speed), "-b", str(brightness)]

        if mode == 0:  # Static mode needs zone and color
            command += ["-z", self.zone_combobox.currentText(), "-cR", str(red), "-cG", str(green), "-cB", str(blue)]
        elif mode in [1, 4, 5]:  # Breath, Shifting, Zoom need only color
            command += ["-cR", str(red), "-cG", str(green), "-cB", str(blue)]
        elif mode == 2:  # Neon doesn't require extra params
            pass
        elif mode == 3:  # Wave needs speed and color
            command += ["-cR", str(red), "-cG", str(green), "-cB", str(blue)]

        print("Running command:", " ".join(command))
        subprocess.run(command)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RGBControlApp()
    window.show()
    sys.exit(app.exec_())
