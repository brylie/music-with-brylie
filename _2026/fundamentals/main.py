"""Main scenes for fundamentals of sound and music theory."""

from manim import *


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

        # Create axes for wave visualization
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE_D},
        )

        # Create a sine wave (representing A440 - standard tuning)
        sine_wave = axes.plot(lambda x: np.sin(x), color=BLUE)

        wave_label = Text("y = sin(x)", font_size=36)
        wave_label.next_to(axes, DOWN, buff=0.5)

        frequency_text = Text("A440 (Standard Tuning)", font_size=32)
        frequency_text.next_to(wave_label, DOWN)

        # Animate wave creation
        self.play(Create(axes))
        self.play(Create(sine_wave), run_time=2)
        self.play(Write(wave_label))
        self.play(FadeIn(frequency_text, shift=UP))

        self.wait(2)

        # Closing
        thank_you = Text("Let's explore sound together!", font_size=40)
        self.play(
            FadeOut(axes),
            FadeOut(sine_wave),
            FadeOut(wave_label),
            FadeOut(frequency_text),
            FadeOut(title),
        )
        self.play(Write(thank_you))
        self.wait(2)


# Define the order scenes should be rendered
SCENES_IN_ORDER = [
    HelloManim,
]
