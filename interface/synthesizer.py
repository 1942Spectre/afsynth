# interface/synthesizer.py
import tkinter as tk
from tkinter import ttk
from interface.options import waveform_selector

class SynthesizerUI:
    def __init__(self, root, label):
        self.frame = ttk.LabelFrame(root, text=label)
        self.frame.pack(fill="x")

        self.waveform_selector = waveform_selector.WaveformSelector(self.frame)
        self.waveform_selector.pack()

    def pack(self):
        self.frame.pack()
