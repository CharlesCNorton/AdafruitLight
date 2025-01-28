import tkinter as tk
from tkinter import messagebox
import serial
import time

# Update the COM port and baud rate
serialPort = 'COM4'  # Replace with your actual COM port
baudRate = 9600

# Tower light commands
RED_ON = 0x11
RED_OFF = 0x21
RED_BLINK = 0x41

YELLOW_ON = 0x12
YELLOW_OFF = 0x22
YELLOW_BLINK = 0x42

GREEN_ON = 0x14
GREEN_OFF = 0x24
GREEN_BLINK = 0x44

BUZZER_ON = 0x18
BUZZER_OFF = 0x28
BUZZER_BLINK = 0x48


class TowerLightController:
    def __init__(self, master):
        self.master = master
        self.master.title("Adafruit Tower Light Controller")

        # Serial connection
        try:
            self.serial = serial.Serial(serialPort, baudRate)
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not open {serialPort}: {e}")
            self.serial = None

        # GUI Layout
        self.create_widgets()

    def create_widgets(self):
        # Red Light Controls
        tk.Label(self.master, text="Red Light").grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.master, text="On", command=lambda: self.send_command(RED_ON)).grid(row=0, column=1, padx=5)
        tk.Button(self.master, text="Off", command=lambda: self.send_command(RED_OFF)).grid(row=0, column=2, padx=5)
        tk.Button(self.master, text="Blink", command=lambda: self.send_command(RED_BLINK)).grid(row=0, column=3, padx=5)

        # Yellow Light Controls
        tk.Label(self.master, text="Yellow Light").grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.master, text="On", command=lambda: self.send_command(YELLOW_ON)).grid(row=1, column=1, padx=5)
        tk.Button(self.master, text="Off", command=lambda: self.send_command(YELLOW_OFF)).grid(row=1, column=2, padx=5)
        tk.Button(self.master, text="Blink", command=lambda: self.send_command(YELLOW_BLINK)).grid(row=1, column=3, padx=5)

        # Green Light Controls
        tk.Label(self.master, text="Green Light").grid(row=2, column=0, padx=10, pady=5)
        tk.Button(self.master, text="On", command=lambda: self.send_command(GREEN_ON)).grid(row=2, column=1, padx=5)
        tk.Button(self.master, text="Off", command=lambda: self.send_command(GREEN_OFF)).grid(row=2, column=2, padx=5)
        tk.Button(self.master, text="Blink", command=lambda: self.send_command(GREEN_BLINK)).grid(row=2, column=3, padx=5)

        # Buzzer Controls
        tk.Label(self.master, text="Buzzer").grid(row=3, column=0, padx=10, pady=5)
        tk.Button(self.master, text="On", command=lambda: self.send_command(BUZZER_ON)).grid(row=3, column=1, padx=5)
        tk.Button(self.master, text="Off", command=lambda: self.send_command(BUZZER_OFF)).grid(row=3, column=2, padx=5)
        tk.Button(self.master, text="Blink", command=lambda: self.send_command(BUZZER_BLINK)).grid(row=3, column=3, padx=5)

        # Exit Button
        tk.Button(self.master, text="Exit", command=self.close).grid(row=4, column=0, columnspan=4, pady=10)

    def send_command(self, command):
        """Send a command to the tower light."""
        if self.serial:
            try:
                self.serial.write(bytes([command]))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send command: {e}")

    def close(self):
        """Close the serial connection and exit."""
        if self.serial:
            try:
                self.serial.close()
            except Exception as e:
                messagebox.showwarning("Warning", f"Could not close serial connection: {e}")
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TowerLightController(root)
    root.mainloop()
