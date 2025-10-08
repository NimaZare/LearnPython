import os
import uuid
import sounddevice as sd
from scipy.io.wavfile import write, read


class VoiceTools:
    def __init__(self):
        pass

    @staticmethod
    def record_audio(duration: int, samplerate: int) -> str:
        """
        Records audio from the microphone for a given duration and sample rate.
        The recorded audio is saved to a uniquely named WAV file in the src/output directory.
        Returns the filename of the saved audio.

        :param duration: Duration of the recording in seconds.
        :type duration: int
        :param samplerate: Sampling rate for the recording.
        :type samplerate: int
        :return: Filename of the saved WAV file.
        :rtype: str
        """
        print("Recording...")
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
        sd.wait()
        print("Recording completed.")
        os.makedirs("VoiceRecorder/src/output", exist_ok=True)
        filename = os.path.join("VoiceRecorder/src/output", f"recorded_{uuid.uuid4().hex[:8]}.wav")
        write(filename, samplerate, audio_data)
        print(f"Audio saved to {filename.replace('/', '\\')}")

    @staticmethod
    def play_audio(filename: str):
        """
        Plays audio from a given WAV file.

        :param filename: Path to the WAV file to be played.
        :type filename: str
        """
        print("Playing audio...")
        samplerate, audio_data = read(filename.strip('"').strip("'").strip())
        sd.play(data=audio_data, samplerate=samplerate)
        sd.wait()
        print("Playback finished.")

