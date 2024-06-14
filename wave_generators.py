import numpy as np

def generate_sine_wave(frequency, t):
    return np.sin(2 * np.pi * frequency * t)

def generate_square_wave(frequency, t):
    return np.sign(generate_sine_wave(frequency, t))

def generate_triangle_wave(frequency, t):
    return 2 * np.arcsin(np.sin(2 * np.pi * frequency * t)) / np.pi

def generate_sawtooth_wave(frequency, t):
    return 2 * (t * frequency - np.floor(0.5 + t * frequency))