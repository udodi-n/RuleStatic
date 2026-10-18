# Image Scraper

Downloads every `<img>` on a page into a local `images/` folder.

## How to use

1. Install dependencies (uses [uv](https://docs.astral.sh/uv/)):

   ```sh
   uv sync
   ```

2. Open `scraper.py` and change the URL at the top:

   ```python
   link = "https://example.com/"
   ```

3. Run it:

   ```sh
   uv run python scraper.py
   ```

4. Images show up in `images/` as `output_image-0.jpg`, `output_image-1.jpg`, ...

## Limitations

- **Static sites only.** It reads the HTML that the server sends back. Any images
  loaded by JavaScript after the page loads are invisible to it.
- Only grabs `<img>` tags with a full `http(s)` URL in `src`. Images added by
  lazy-loading (`data-src`, `srcset`) or CSS backgrounds are skipped.
- Saves everything as `.jpg`, even if the file is really a `.png` or `.webp`.
- No errors, no progress, no rate limiting — it just runs.

