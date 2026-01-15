"""Universal imports for music-with-brylie manim project.

This file provides a single import point for all common dependencies.
Import this in your scene files instead of importing manim directly.
"""

# Core manim imports
# Standard library imports commonly used in scenes
import numpy as np
from manim import *

# Custom components
from custom.audio_mobjects import FrequencySpectrum, SoundWave

__all__ = [
    "SoundWave",
    "FrequencySpectrum",
    "np",
]
