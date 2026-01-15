"""Tests for audio utility functions and mobjects."""

import os

import numpy as np
from scipy.io import wavfile

from utils.audio_mobjects import compute_frequency_spectrum, generate_tone


class TestGenerateTone:
    """Tests for generate_tone function."""

    def test_generates_wav_file(self):
        """Test that generate_tone creates a valid WAV file."""
        audio_file = generate_tone(frequency=440, duration=1, amplitude=0.5)

        assert os.path.exists(audio_file)
        assert audio_file.endswith(".wav")

        # Clean up
        os.unlink(audio_file)

    def test_wav_file_properties(self):
        """Test that the generated WAV file has correct properties."""
        frequency = 440
        duration = 2
        sample_rate = 44100
        amplitude = 0.5

        audio_file = generate_tone(
            frequency=frequency,
            duration=duration,
            sample_rate=sample_rate,
            amplitude=amplitude,
        )

        # Read the WAV file
        rate, data = wavfile.read(audio_file)

        assert rate == sample_rate
        assert len(data) == int(sample_rate * duration)
        assert data.dtype == np.int16

        # Check amplitude is within expected range
        # 16-bit audio ranges from -32768 to 32767
        max_amplitude = np.max(np.abs(data))
        expected_max = amplitude * 32767
        assert abs(max_amplitude - expected_max) < 100  # Allow small tolerance

        # Clean up
        os.unlink(audio_file)

    def test_different_frequencies(self):
        """Test generating tones at different frequencies."""
        frequencies = [220, 440, 880]  # A3, A4, A5

        for freq in frequencies:
            audio_file = generate_tone(frequency=freq, duration=0.5)
            assert os.path.exists(audio_file)
            os.unlink(audio_file)

    def test_different_durations(self):
        """Test generating tones with different durations."""
        durations = [0.5, 1.0, 2.0]
        sample_rate = 44100

        for duration in durations:
            audio_file = generate_tone(frequency=440, duration=duration, sample_rate=sample_rate)
            _rate, data = wavfile.read(audio_file)

            expected_samples = int(sample_rate * duration)
            assert len(data) == expected_samples

            os.unlink(audio_file)

    def test_amplitude_range(self):
        """Test that amplitude parameter controls volume."""
        amplitudes = [0.1, 0.5, 1.0]

        for amp in amplitudes:
            audio_file = generate_tone(frequency=440, duration=1, amplitude=amp)
            _, data = wavfile.read(audio_file)

            max_value = np.max(np.abs(data))
            expected_max = amp * 32767

            # Allow 5% tolerance
            assert abs(max_value - expected_max) < expected_max * 0.05

            os.unlink(audio_file)


class TestComputeFrequencySpectrum:
    """Tests for compute_frequency_spectrum function."""

    def test_returns_arrays(self):
        """Test that the function returns frequency and magnitude arrays."""
        frequencies, magnitudes = compute_frequency_spectrum(frequency=440, duration=1)

        assert isinstance(frequencies, np.ndarray)
        assert isinstance(magnitudes, np.ndarray)
        assert len(frequencies) == len(magnitudes)

    def test_peak_at_correct_frequency(self):
        """Test that the spectrum has a peak at the input frequency."""
        test_freq = 440
        frequencies, magnitudes = compute_frequency_spectrum(
            frequency=test_freq, duration=2, amplitude=0.5
        )

        # Find the peak
        peak_idx = np.argmax(magnitudes)
        peak_freq = frequencies[peak_idx]

        # The peak should be close to the input frequency
        # Allow some tolerance due to FFT bin resolution
        assert abs(peak_freq - test_freq) < 5  # Within 5 Hz

    def test_pure_tone_has_single_peak(self):
        """Test that a pure tone produces a single dominant peak."""
        _frequencies, magnitudes = compute_frequency_spectrum(frequency=440, duration=2)

        # Find peaks above 10% of max magnitude
        max_mag = np.max(magnitudes)
        significant_peaks = magnitudes > (0.1 * max_mag)

        # For a pure tone, we should have very few significant peaks
        # (ideally just one, but FFT can show some spread)
        assert np.sum(significant_peaks) < 20

    def test_different_frequencies(self):
        """Test spectrum computation for different frequencies."""
        test_frequencies = [220, 440, 880]

        for test_freq in test_frequencies:
            frequencies, magnitudes = compute_frequency_spectrum(frequency=test_freq, duration=2)

            peak_idx = np.argmax(magnitudes)
            peak_freq = frequencies[peak_idx]

            assert abs(peak_freq - test_freq) < 5

    def test_frequency_range(self):
        """Test that frequencies are in expected range."""
        frequencies, _magnitudes = compute_frequency_spectrum(
            frequency=440, duration=1, sample_rate=44100
        )

        # Frequencies should start at 0
        assert frequencies[0] == 0

        # Maximum frequency should be Nyquist frequency (sample_rate / 2)
        assert frequencies[-1] <= 22050

    def test_amplitude_affects_magnitude(self):
        """Test that amplitude parameter affects the magnitude of the spectrum."""
        freq = 440
        duration = 2

        _, mag_low = compute_frequency_spectrum(freq, duration, amplitude=0.1)
        _, mag_high = compute_frequency_spectrum(freq, duration, amplitude=0.5)

        # Higher amplitude should produce higher magnitude
        assert np.max(mag_high) > np.max(mag_low)

    def test_longer_duration_better_resolution(self):
        """Test that longer duration provides better frequency resolution."""
        freq = 440

        freq_short, _ = compute_frequency_spectrum(freq, duration=0.5, sample_rate=44100)
        freq_long, _ = compute_frequency_spectrum(freq, duration=2, sample_rate=44100)

        # Longer duration should have finer frequency spacing
        spacing_short = freq_short[1] - freq_short[0]
        spacing_long = freq_long[1] - freq_long[0]

        assert spacing_long < spacing_short
