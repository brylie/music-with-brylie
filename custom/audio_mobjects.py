"""Custom Manim mobjects for audio and music visualization."""

import tempfile

import numpy as np
from manim import *
from scipy.io import wavfile


def generate_tone(frequency, duration=2, sample_rate=44100, amplitude=0.5):
    """Generate a pure tone and save to temporary WAV file.

    Args:
        frequency: Frequency in Hz (e.g., 440 for A4)
        duration: Duration in seconds
        sample_rate: Samples per second
        amplitude: Volume (0.0 to 1.0)

    Returns:
        Path to temporary WAV file
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio_data = amplitude * np.sin(2 * np.pi * frequency * t)

    # Convert to 16-bit PCM
    audio_data = (audio_data * 32767).astype(np.int16)

    # Save to temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wavfile.write(temp_file.name, sample_rate, audio_data)
    temp_file.close()

    return temp_file.name


class SoundWave(VGroup):
    """Custom mobject for sound wave visualization.

    Args:
        frequency: Frequency in Hz (default: 440 for A4)
        amplitude: Wave amplitude (default: 1)
        duration: Duration in seconds (default: 2)
        sample_rate: Samples per second (default: 44100)
        color: Wave color (default: BLUE)
    """

    def __init__(
        self,
        frequency=440,
        amplitude=1,
        duration=2,
        sample_rate=44100,
        color=BLUE,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sample_rate = sample_rate

        # Create axes
        self.axes = Axes(
            x_range=[0, duration, duration / 4],
            y_range=[-amplitude * 1.5, amplitude * 1.5, amplitude / 2],
            x_length=10,
            y_length=4,
            axis_config={"color": GREY_D},
        )

        # Create wave
        self.wave = self.axes.plot(
            lambda t: amplitude * np.sin(2 * PI * frequency * t),
            x_range=[0, duration],
            color=color,
        )

        self.add(self.axes, self.wave)

    def get_audio_file(self):
        """Generate and return path to audio file for this waveform."""
        return generate_tone(self.frequency, self.duration, amplitude=self.amplitude)


class FrequencySpectrum(VGroup):
    """Visualization of frequency spectrum (placeholder for future development)."""

    def __init__(self, frequencies, amplitudes, **kwargs):
        super().__init__(**kwargs)
        # TODO: Implement frequency spectrum visualization
        pass
