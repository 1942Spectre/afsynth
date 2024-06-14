import interface
import synthesizer
import mido


def main():
    print(mido.get_input_names()[0])  # List available MIDI devices
    interface.create_interface()
    synthesizer.start_synth(mido.get_input_names()[0])

if __name__ == "__main__":
    main()