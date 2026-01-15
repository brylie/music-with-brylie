"""Common reusable scenes for all videos."""

from manim import *


class Credits(Scene):
    """Standard credits scene for all videos.

    Displays licensing information:
    - Creative Commons Attribution 4.0+ for video content
    - MIT license for source code
    - GitHub repository URL
    """

    def construct(self):
        # Title
        title = Text("Credits & Licensing", font_size=48)
        title.to_edge(UP, buff=0.5)

        # Content license
        content_license_title = Text("Video Content:", font_size=36, color=BLUE)
        content_license_title.next_to(title, DOWN, buff=0.8)

        cc_by = Text(
            "Creative Commons Attribution 4.0 International (CC BY 4.0+)",
            font_size=28,
        )
        cc_by.next_to(content_license_title, DOWN, buff=0.3)

        cc_details = Text(
            "You are free to share and adapt with attribution",
            font_size=24,
            color=GRAY,
        )
        cc_details.next_to(cc_by, DOWN, buff=0.2)

        # Source code license
        code_license_title = Text("Source Code:", font_size=36, color=GREEN)
        code_license_title.next_to(cc_details, DOWN, buff=0.6)

        mit_license = Text("MIT License", font_size=28)
        mit_license.next_to(code_license_title, DOWN, buff=0.3)

        # GitHub URL
        github_url = Text(
            "github.com/brylie/music-with-brylie",
            font_size=28,
            color=YELLOW,
        )
        github_url.next_to(mit_license, DOWN, buff=0.6)

        # Thank you message
        thank_you = Text("Thank you for watching!", font_size=32, color=GRAY)
        thank_you.to_edge(DOWN, buff=0.5)

        # Animations
        self.play(Write(title))
        self.wait(0.5)

        self.play(
            FadeIn(content_license_title, shift=DOWN * 0.5),
            FadeIn(cc_by, shift=DOWN * 0.5),
        )
        self.play(FadeIn(cc_details))
        self.wait(1)

        self.play(
            FadeIn(code_license_title, shift=DOWN * 0.5),
            FadeIn(mit_license, shift=DOWN * 0.5),
        )
        self.wait(0.5)

        self.play(Write(github_url))
        self.wait(1)

        self.play(FadeIn(thank_you, shift=UP * 0.5))
        self.wait(3)
