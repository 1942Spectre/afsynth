# interface/circle.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def relative_minor(note):
    note_index = notes.index(note)
    minor_index = (note_index + 9) % 12
    return notes[minor_index]

def generate_circle_of_fifths(root_note):
    root_index = notes.index(root_note)
    circle = []
    for i in range(12):
        major_note = notes[(root_index + 7 * i) % 12]
        minor_note = relative_minor(major_note)
        circle.append((major_note, minor_note))
    return circle

def note_to_label(freq):
    midi_note = round(12 * np.log2(freq / 440.0) + 69)
    note_labels = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return note_labels[midi_note % 12]

class CircleOfFifths:
    def __init__(self, root):
        self.root_note = root
        self.circle_of_fifths_labels = generate_circle_of_fifths(self.root_note)
        self.circle_of_fifths_angles = np.linspace(0, 2 * np.pi, 12, endpoint=False)
        self.circle_of_fifths_coords_major = [(np.sin(angle), np.cos(angle)) for angle in self.circle_of_fifths_angles]
        self.circle_of_fifths_coords_minor = [(np.sin(angle) * 0.75, np.cos(angle) * 0.75) for angle in self.circle_of_fifths_angles]

    def update_circle_of_fifths(self, ax, active_notes):
        ax.clear()
        ax.set_aspect('equal')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')

        for i, (major, minor) in enumerate(self.circle_of_fifths_labels):
            major_x, major_y = self.circle_of_fifths_coords_major[i]
            minor_x, minor_y = self.circle_of_fifths_coords_minor[i]

            if major in [note_to_label(frequency) for frequency in active_notes]:
                ax.text(major_x, major_y, major, ha='center', va='center', fontsize=12, color='red')
            else:
                ax.text(major_x, major_y, major, ha='center', va='center', fontsize=12)

            if minor in [note_to_label(frequency) for frequency in active_notes]:
                ax.text(minor_x, minor_y, minor, ha='center', va='center', fontsize=12, color='red')
            else:
                ax.text(minor_x, minor_y, minor, ha='center', va='center', fontsize=12)

        return ax

    def render(self, root):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.axis('off')

        for i, (major, minor) in enumerate(self.circle_of_fifths_labels):
            major_x, major_y = self.circle_of_fifths_coords_major[i]
            minor_x, minor_y = self.circle_of_fifths_coords_minor[i]

            self.ax.text(major_x, major_y, major, ha='center', va='center', fontsize=12)
            self.ax.text(minor_x, minor_y, minor, ha='center', va='center', fontsize=12)

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        return self.canvas.get_tk_widget(), self.ax