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
mise run render src/_2026/fundamentals/main.py HelloManim

# High quality (slower)
mise run render-hq src/_2026/fundamentals/main.py HelloManim
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

### Code Quality

The project includes comprehensive code quality tools:

```bash
# Format code (Python with ruff, other files with dprint)
mise run format

# Lint code (ruff for Python, dprint for markdown/YAML/TOML/JSON)
mise run lint

# Type check (mypy)
mise run typecheck

# Run all CI checks (tests + lint + typecheck)
mise run ci
```

### Git Hooks

The project uses [lefthook](https://github.com/evilmartians/lefthook) for automated quality checks:

- **pre-commit**: Auto-formats Python (ruff) and other files (dprint) on staged changes
- **pre-push**: Runs full CI suite
  - Format checking (ruff + dprint)
  - Linting (ruff)
  - Type checking (mypy)
  - Tests with minimum 60% coverage requirement

Git hooks are automatically installed when you run `mise install`. The pre-push hook ensures code quality before pushing to remote.

## Project Structure

```
music-with-brylie/
├── src/                      # Source code (src layout)
│   ├── _2026/               # Videos organized by year
│   │   └── fundamentals/    # Topic-based folders
│   │       ├── __init__.py
│   │       └── main.py      # Main scenes
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── audio_mobjects.py # Audio utilities
├── tests/                    # Test suite
│   ├── __init__.py
│   └── test_audio_mobjects.py
└── mise.toml                # Development tools configuration
```

This project follows Python best practices and 3Blue1Brown's organizational approach:

- **Src layout**: Source code in `src/` directory for clean imports
- **Year-based organization**: Videos organized by year, then topic
- **Reusable utilities**: Utility functions in `src/utils/` directory
- **Scene ordering**: Use `SCENES_IN_ORDER` to define rendering order
- **Test coverage**: Tests in `tests/` directory with pytest

### Adding New Videos

1. Create a new folder under `src/_2026/` (e.g., `src/_2026/acoustics/`)
2. Add `__init__.py` and `main.py` to the new folder
3. Define your scenes in `main.py`
4. Add to `SCENES_IN_ORDER` list
5. Render with `mise run render src/_2026/acoustics/main.py SceneName`

### Adding Utility Functions

Place reusable utility functions in the `src/utils/` directory. Add corresponding tests in `tests/` and run `mise run test` to verify.

### Using the Credits Scene

A standard Credits scene is available in `src/utils/common_scenes.py` that displays:

- Creative Commons Attribution 4.0+ license for video content
- MIT license for source code
- GitHub repository URL

To render it:

```bash
mise run render src/utils/common_scenes.py Credits
```

Import it in your scenes to include at the end of videos:

```python
from utils.common_scenes import Credits

# In your SCENES_IN_ORDER list:
SCENES_IN_ORDER = [
    YourScene,
    Credits,
]
```

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
