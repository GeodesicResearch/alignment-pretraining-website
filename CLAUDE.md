# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the website for the Alignment Pretraining research paper hosted at alignmentpretraining.ai. It's a static website showcasing research on how AI discourse in pretraining data causes self-fulfilling prophecies in model alignment behavior.

## Key Files

- `index.html` - Main page with research content, author information, and artifacts table
- `styles.css` - CSS styling with responsive design and print styles
- `alignment_pretraining.pdf` - The research paper
- `images/` - Research figures (hero.png, base_model_results.png, benchmark_example_hero.png, favicon.png)
- `CNAME` - GitHub Pages custom domain (alignmentpretraining.ai)

## Content Structure

The website presents:
1. Paper abstract and key findings about self-fulfilling alignment/misalignment
2. Visual results showing the effects of upsampling alignment/misalignment discourse
3. Released model artifacts table (4 base model variants + post-trained versions + datasets)
4. Citation information in BibTeX format

## Development

Static website with no build process. Changes to HTML/CSS take effect immediately.

### Local Development
```bash
# Serve locally with Python
python3 -m http.server 8000

# Or with Node.js http-server if available
npx http-server
```

### Testing Responsiveness
The site uses responsive CSS breakpoints at 768px and 480px. Test at various viewport sizes.

## Deployment

GitHub Pages deployment from main branch. Commits to main automatically deploy to alignmentpretraining.ai.

## Style Guidelines

- Primary color: `#154d39` (deep green) used for headings and emphasis
- Font: Poppins for headings, system fonts for body text
- All external links open in new tabs (`target="_blank"`)
- Images use descriptive alt text for accessibility
- Tables use semantic HTML with proper header structure

## Paper Color Scheme

The paper uses the following color palette:
- Light Red: RGB(244,67,54) / #f44336
- Light Blue: RGB(30,136,229) / #1e88e5
- Geodesic Beige: RGB(151,86,84) / #975654
- Geodesic Blue: RGB(188,209,202) / #bcd1ca
- Bar Coral: RGB(232,132,107) / #e8846b
- Bar Coral Dark: RGB(214,95,69) / #d65f45
- Bar Blue Light: RGB(157,207,234) / #9dcfea
- Bar Blue Dark: RGB(61,122,184) / #3d7ab8