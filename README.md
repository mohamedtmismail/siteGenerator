# siteGenerator
A small static-site generator written in Python. Markdown files under `content/` are converted to HTML files in `docs/` using `template.html`. Files from `static/` are copied to the output directory unchanged.

## Project Structure

```
.
├── content/       # Markdown pages and posts
├── docs/          # Generated site (HTML & CSS)
├── src/           # Generator source code and unit tests
├── static/        # Assets copied as-is to docs/
├── template.html  # Base HTML template
├── build.sh       # Build script
├── main.sh        # Build + run dev server
└── test.sh        # Run unit tests
```

## How to run

1. **Build the site**

   ```bash
   ./build.sh
   ```

   This will remove the old `docs/` folder, copy assets from `static/`, and generate HTML from the Markdown files in `content/`.

   To change the base URL used for links, run `python3 src/main.py <basepath>` instead.

2. **Serve locally**

   ```bash
   ./main.sh
   ```

   After generating the site, a development server is started at `http://localhost:8888` so you can preview the output.

3. **Run tests**

   ```bash
   ./test.sh
   ```

   Executes the unit tests under `src/` to verify Markdown parsing and HTML generation.

The scripts above rely only on Python's standard library, so no extra dependencies are required.

## Live static site

You can see the static generated site [here](https://mohamedtmismail.github.io/siteGenerator/)

## Architecture

![staticArchitecture](https://github.com/user-attachments/assets/09bb3053-a99d-407e-bff3-a16c2a7f6060)

![mdtonodestohtml](https://github.com/user-attachments/assets/7f1e510d-f304-4b86-8b33-55ff05a2db19)


> This project is part of [boot.dev](https://boot.dev)
