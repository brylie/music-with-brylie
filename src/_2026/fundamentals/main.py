"""Main scenes for fundamentals of sound and music theory."""

import atexit
import os

from manim import *

from utils.audio_mobjects import compute_frequency_spectrum, generate_tone
from utils.common_scenes import Credits


class HelloManim(Scene):
    """Introduction scene demonstrating a simple sound wave visualization."""

    def construct(self):
        # Create title
        title = Text("Music with Brylie", font_size=60)
        title.to_edge(UP)

        subtitle = Text("Exploring Sound with Manim", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.5)

        # Animate title
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait()

        # Transition title
        self.play(
            title.animate.scale(0.6).to_corner(UL),
            FadeOut(subtitle),
        )

        # Create time domain axes (left side)
        time_axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=3,
            axis_config={"color": BLUE_D},
            tips=False,
        ).shift(LEFT * 3.5)

        # Add axis labels with units for time domain
        time_axes.add_coordinates(
            {
                0: "0",
                PI: MathTex(r"\pi"),
                2 * PI: MathTex(r"2\pi"),
                3 * PI: MathTex(r"3\pi"),
                4 * PI: MathTex(r"4\pi"),
            },
            direction=DOWN,
            font_size=16,
        )
        time_axes.get_y_axis().add_numbers(
            [-1, 0, 1],
            direction=LEFT,
            font_size=16,
        )

        time_label = Text("Time Domain", font_size=28)
        time_label.next_to(time_axes, UP, buff=0.3)

        time_x_label = Text("Time (radians)", font_size=20)
        time_x_label.next_to(time_axes, DOWN, buff=0.5)

        time_y_label = Text("Amplitude", font_size=20)
        time_y_label.rotate(90 * DEGREES)
        time_y_label.next_to(time_axes, LEFT, buff=0.3)

        # Create frequency domain axes (right side)
        freq_axes = Axes(
            x_range=[0, 1000, 200],
            y_range=[0, 0.6, 0.2],
            x_length=5,
            y_length=3,
            axis_config={"color": GREEN_D},
            tips=False,
        ).shift(RIGHT * 3.5)

        # Add axis labels with units for frequency domain
        freq_axes.get_x_axis().add_numbers(
            [0, 200, 400, 600, 800, 1000],
            direction=DOWN,
            font_size=16,
        )
        freq_axes.get_y_axis().add_numbers(
            [0, 0.2, 0.4, 0.6],
            direction=LEFT,
            font_size=16,
            num_decimal_places=1,
        )

        freq_label = Text("Frequency Domain", font_size=28)
        freq_label.next_to(freq_axes, UP, buff=0.3)

        freq_x_label = Text("Frequency (Hz)", font_size=20)
        freq_x_label.next_to(freq_axes, DOWN, buff=0.5)

        freq_y_label = Text("Magnitude", font_size=20)
        freq_y_label.rotate(90 * DEGREES)
        freq_y_label.next_to(freq_axes, LEFT, buff=0.3)

        # Create sine wave
        sine_wave = time_axes.plot(lambda x: np.sin(x), color=BLUE)

        # Compute and create frequency spectrum
        frequencies, magnitudes = compute_frequency_spectrum(
            frequency=440, duration=2, amplitude=0.5
        )

        # Create frequency spectrum line graph
        freq_points = []
        for f, m in zip(frequencies, magnitudes, strict=True):
            if 0 <= f <= 1000:  # Only plot up to 1000 Hz
                freq_points.append(freq_axes.c2p(f, m))

        if len(freq_points) > 1:
            freq_spectrum = VMobject(color=GREEN)
            freq_spectrum.set_points_as_corners(freq_points)
        else:
            freq_spectrum = VMobject()

        frequency_text = Text("A440 (Standard Tuning)", font_size=28)
        frequency_text.to_edge(DOWN, buff=0.5)

        # Animate both domains
        self.play(
            Create(time_axes),
            Create(freq_axes),
            Write(time_label),
            Write(freq_label),
            Write(time_x_label),
            Write(time_y_label),
            Write(freq_x_label),
            Write(freq_y_label),
        )

        # Generate and play A440 tone during visualization creation
        a440_audio = generate_tone(frequency=440, duration=2, amplitude=0.3)

        # Register cleanup to run after Manim's SceneFileWriter finalization
        atexit.register(lambda: os.path.exists(a440_audio) and os.unlink(a440_audio))

        self.add_sound(a440_audio)
        self.play(Create(sine_wave), Create(freq_spectrum), run_time=2)
        self.play(FadeIn(frequency_text, shift=UP))

        self.wait(2)

        # Closing
        thank_you = Text("Let's explore sound together!", font_size=40)
        self.play(
            FadeOut(time_axes),
            FadeOut(freq_axes),
            FadeOut(sine_wave),
            FadeOut(freq_spectrum),
            FadeOut(time_label),
            FadeOut(freq_label),
            FadeOut(time_x_label),
            FadeOut(time_y_label),
            FadeOut(freq_x_label),
            FadeOut(freq_y_label),
            FadeOut(frequency_text),
            FadeOut(title),
        )
        self.play(Write(thank_you))
        self.wait(2)


# Define the order scenes should be rendered
SCENES_IN_ORDER = [
    HelloManim,
    Credits,
]
