# interface/options/waveform_selector.py
import tkinter as tk
from tkinter import ttk
import wave_generators

class WaveformSelector(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ttk.Label(self, text="Waveform")
        self.label.pack(side="left")

        self.waveform_var = tk.StringVar(self)
        self.waveform_var.set("Sine")
        waveforms = ["Sine", "Square", "Triangle", "Sawtooth"]

        self.waveform_menu = ttk.OptionMenu(self, self.waveform_var, self.waveform_var.get(), *waveforms)
        self.waveform_menu.pack(side="right")

    def get_waveform(self):
        waveform = self.waveform_var.get()
        if waveform == "Sine":
            return wave_generators.generate_sine_wave
        elif waveform == "Square":
            return wave_generators.generate_square_wave
        elif waveform == "Triangle":
            return wave_generators.generate_triangle_wave
        elif waveform == "Sawtooth":
            return wave_generators.generate_sawtooth_wave