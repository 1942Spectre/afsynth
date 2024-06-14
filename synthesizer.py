# synthesizer.py
import sounddevice as sd
import mido
import callbacks
import interface

SAMPLE_RATE = 44100  

def start_synth(midi_device):
    midi_input = mido.open_input(midi_device, callback=callbacks.midi_callback)

    with sd.OutputStream(callback=callbacks.audio_callback, samplerate=SAMPLE_RATE, channels=1):
        print(f"Listening to MIDI device: {midi_device}")
        interface.tk.mainloop()