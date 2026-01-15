"""Custom Manim mobjects for audio and music visualization."""

import numpy as np
from manim import *


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


class FrequencySpectrum(VGroup):
    """Visualization of frequency spectrum (placeholder for future development)."""

    def __init__(self, frequencies, amplitudes, **kwargs):
        super().__init__(**kwargs)
        # TODO: Implement frequency spectrum visualization
        pass
