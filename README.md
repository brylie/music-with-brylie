# music-with-brylie
Educational materials about music.

## Prerequisites

- [mise](https://mise.jdx.dev/) - Manages Python, uv, and project dependencies

## Setup

mise handles all tool installation and dependency management:

```bash
# Install Python and uv (managed by mise)
mise install

# Install Python dependencies
mise run setup
```

## Development

Run the development command:
```bash
mise run dev
```

## Troubleshooting

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
