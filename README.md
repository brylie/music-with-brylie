# music-with-brylie
Educational materials about music.

## Prerequisites

- [mise](https://mise.jdx.dev/) - Tool version manager
- FFmpeg 7 - Required for manim video rendering
  - macOS: `brew install ffmpeg@7`
  - Linux: `apt install ffmpeg` or equivalent
  - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Setup

1. Install FFmpeg (see Prerequisites above)

2. Install mise tools (Python and uv):
   ```bash
   mise install
   ```

3. Install Python dependencies:
   ```bash
   mise run setup
   ```
   
   Or manually:
   ```bash
   uv sync
   ```

## Development

Run the development command:
```bash
mise run dev
```

## Project Structure

This project uses:
- **mise** for Python version management and task automation
- **uv** for fast Python package management
- **manim** for creating mathematical animations

## License

- Code: MIT License (see [LICENSE](LICENSE))
- Content: Creative Commons Attribution 4.0 International (see [LICENSE-content.md](LICENSE-content.md))
