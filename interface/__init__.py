# interface/__init__.py
import tkinter as tk
from tkinter import ttk
from interface.circle import CircleOfFifths
from interface.synthesizer import SynthesizerUI

active_notes = []
current_waveform_1 = None
current_waveform_2 = None
mix_value = 0.5
midi_to_freq = {21: 27.5000, 22: 29.1352, 23: 30.8677, 108: 4186.01}

def update_circle():
    global circle, active_notes, ax
    ax = circle.update_circle_of_fifths(ax, active_notes)
    circle.canvas.draw()

def waveform_selector_callback_1(event):
    global current_waveform_1
    current_waveform_1 = synth_1.waveform_selector.get_waveform()

def waveform_selector_callback_2(event):
    global current_waveform_2
    current_waveform_2 = synth_2.waveform_selector.get_waveform()

def mix_value_changed(val):
    global mix_value
    mix_value = float(val) / 100

def on_close():
    print("Closing the application...")
    root.destroy()
    exit(0)

def create_interface():
    global root, circle, ax, canvas_widget, synth_1, synth_2, mix_slider

    root = tk.Tk()
    root.title("Digital Synthesizer")

    # Circle of Fifths
    circle = CircleOfFifths("C")
    canvas_widget, ax = circle.render(root)
    canvas_widget.pack()

    # Synthesizer 1
    synth_1 = SynthesizerUI(root, "Synthesizer 1")
    synth_1.pack()

    synth_1.waveform_selector.waveform_menu.bind("<Configure>", waveform_selector_callback_1)

    # Synthesizer 2
    synth_2 = SynthesizerUI(root, "Synthesizer 2")
    synth_2.pack()

    synth_2.waveform_selector.waveform_menu.bind("<Configure>", waveform_selector_callback_2)

    # Mix Slider
    mix_frame = ttk.Frame(root)
    mix_frame.pack(fill="x")

    mixer_label = ttk.Label(mix_frame, text="Mix")
    mixer_label.pack(side="left")

    mix_slider = tk.Scale(mix_frame, from_=0, to=100, orient="horizontal", command=mix_value_changed)
    mix_slider.set(50)
    mix_slider.pack(side="right", fill="x", expand=True)

    root.protocol("WM_DELETE_WINDOW", on_close)

if __name__ == "__main__":
    create_interface()
    tk.mainloop()

midi_to_freq = {
    127:12543.85,
    126:11839.82,
    125:11175.30,
    124:10548.08,
    123:9956.06,
    122:9397.27,
    121:8869.84,
    120:8372.02,
    119:7902.13,
    118:7458.62,
    117:7040.00,
    116:6644.88,
    115:6271.93,
    114:5919.91,
    113:5587.65,
    112:5274.04,
    111:4978.03,
    110:4698.64,
    109:4434.92,
    108:4186.01,
    107:3951.07,
    106:3729.31,
    105:3520.00,
    104:3322.44,
    103:3135.96,
    102:2959.96,
    101:2793.83,
    100:2637.02,
    99:2489.02,
    98:2349.32,
    97:2217.46,
    96:2093.00,
    95:1975.53,
    94:1864.66,
    93:1760.00,
    92:1661.22,
    91:1567.98,
    90:1479.98,
    89:1396.91,
    88:1318.51,
    87:1244.51,
    86:1174.66,
    85:1108.73,
    84:1046.50,
    83:987.77,
    82:932.33,
    81:880.00,
    80:830.61,
    79:783.99,
    78:739.99,
    77:698.46,
    76:659.26,
    75:622.25,
    74:587.33,
    73:554.37,
    72:523.25,
    71:493.88,
    70:466.16,
    69:440.00,
    68:415.30,
    67:392.00,
    66:369.99,
    65:349.23,
    64:329.63,
    63:311.13,
    62:293.66,
    61:277.18,
    60:261.63,
    59:246.94,
    58:233.08,
    57:220.00,
    56:207.65,
    55:196.00,
    54:185.00,
    53:174.61,
    52:164.81,
    51:155.56,
    50:146.83,
    49:138.59,
    48:130.81,
    47:123.47,
    46:116.54,
    45:110.00,
    44:103.83,
    43:98.00,
    42:92.50,
    41:87.31,
    40:82.41,
    39:77.78,
    38:73.42,
    37:69.30,
    36:65.41,
    35:61.74,
    34:58.27,
    33:55.00,
    32:51.91,
    31:49.00,
    30:46.25,
    29:43.65,
    28:41.20,
    27:38.89,
    26:36.71,
    25:34.65,
    24:32.70,
    23:30.87,
    22:29.14,
    21:27.50,
    20 :25.96,
    19 :24.50,
    18 :23.12,
    17 :21.83,
    16 :20.60,
    15 :19.45,
    14 :18.35,
    13 :17.32,
    12 :16.35,
    11 :15.43,
    10 :14.57,
    9 :13.75,
    8 :12.98,
    7 :12.25,
    6 :11.56,
    5 :10.91,
    4 :10.30,
    3 :9.72,
    2 :9.18,
    1 :8.66,
    0 :8.18,
}