# music-with-brylie
Educational materials about music.

## Prerequisites

- [mise](https://mise.jdx.dev/) - Manages Python, uv, FFmpeg, TinyTeX, and project dependencies

## Setup

mise handles all tool installation and dependency management:

```bash
# Install Python, uv, FFmpeg, and TinyTeX (managed by mise)
mise install

# Install Python dependencies
mise run setup
```

**Note**: TinyTeX provides LaTeX support for mathematical notation in manim. It automatically installs needed packages on first use.

## Development

### Rendering Scenes

To render the HelloManim scene:

```bash
# Low quality preview (fast)
mise run render _2026/fundamentals/main.py HelloManim

# High quality (slower)
mise run render-hq _2026/fundamentals/main.py HelloManim
```

The rendered video will be in `media/videos/fundamentals/`.

### Development Command

Run the development check:
```bash
mise run dev
```

### Running Tests

Run the test suite with coverage:
```bash
mise run test
```

## Project Structure

```
music-with-brylie/
├── _2026/                    # Videos organized by year
│   └── fundamentals/         # Topic-based folders
│       ├── __init__.py
│       └── main.py          # Main scenes
├── utils/                    # Utility functions
│   ├── __init__.py
│   └── audio_mobjects.py    # Audio utilities and mobjects
├── tests/                    # Test suite
│   ├── __init__.py
│   └── test_audio_mobjects.py
├── manim_imports_ext.py     # Universal imports
└── mise.toml                # Development tools configuration
```

This project follows the organizational approach pioneered by 3Blue1Brown:
- **Year-based organization**: Videos organized by year, then topic
- **Reusable utilities**: Utility functions in `utils/` directory
- **Scene ordering**: Use `SCENES_IN_ORDER` to define rendering order
- **Universal imports**: Import `manim_imports_ext.py` instead of manim directly
- **Test coverage**: Tests in `tests/` directory with pytest

### Adding New Videos

1. Create a new folder under `_2026/` (e.g., `_2026/acoustics/`)
2. Add `__init__.py` and `main.py` to the new folder
3. Define your scenes in `main.py`
4. Add to `SCENES_IN_ORDER` list
5. Render with `mise run render _2026/acoustics/main.py SceneName`

### Adding Utility Functions

Place reusable utility functions in the `utils/` directory. Add corresponding tests in `tests/` and run `mise run test` to verify.

## Technologies

This project uses:
- **mise** for Python version management and task automation
- **uv** for fast Python package management
- **manim** for creating mathematical animations
- **scipy** for audio synthesis and signal processing (generate tones, waveforms)
- **pytest** for testing with coverage reporting


### FFmpeg Installation Issues

If manim fails to install due to missing FFmpeg, you'll need to install FFmpeg 7 manually:

**macOS:**
```bash
brew install ffmpeg@7
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora/RHEL
sudo dnf install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html)

After installing FFmpeg, run:
```bash
mise run setup
```

### Manual Tool Installation

If you prefer not to use mise, you can install tools manually:

1. Install Python 3.13
2. Install uv: `pip install uv`
3. Install FFmpeg 7 (see above)
4. Install dependencies: `uv sync`

## Project Structure

This project uses:
- **mise** for Python version management and task automation
- **uv** for fast Python package management
- **manim** for creating mathematical animations

## License

- Code: MIT License (see [LICENSE](LICENSE))
- Content: Creative Commons Attribution 4.0 International (see [LICENSE-content.md](LICENSE-content.md))
