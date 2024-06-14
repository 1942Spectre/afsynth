# callbacks.py
import numpy as np
import interface

SAMPLE_RATE = 44100

def midi_callback(msg):
    if msg.type == 'note_on' and msg.velocity > 0:
        if interface.midi_to_freq[msg.note] not in interface.active_notes:
            interface.active_notes.append(interface.midi_to_freq[msg.note])
            interface.update_circle()
    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
        if interface.midi_to_freq[msg.note] in interface.active_notes:
            interface.active_notes.remove(interface.midi_to_freq[msg.note])
            interface.update_circle()

def audio_callback(outdata, frames, time, status):
    current_waveform_1 = interface.current_waveform_1
    current_waveform_2 = interface.current_waveform_2
    mix_value = interface.mix_value

    if not current_waveform_1 or not current_waveform_2:
        outdata[:] = np.zeros(frames).reshape(-1, 1)
        return

    if interface.active_notes:
        t = np.linspace(0, frames / SAMPLE_RATE, frames, endpoint=False)
        waveform_1 = np.zeros(frames)
        waveform_2 = np.zeros(frames)

        for frequency in interface.active_notes:
            waveform_1 += 0.5 * current_waveform_1(frequency, t)
            waveform_2 += 0.5 * current_waveform_2(frequency, t)
        
        waveform = (waveform_1 * mix_value) + (waveform_2 * (1 - mix_value))
    else:
        waveform = np.zeros(frames)

    outdata[:] = waveform.reshape(-1, 1)