# PDF Comment Extractor

This script extracts all comments and annotations from the Alignment Pretraining paper PDF hosted on Google Drive.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python extract_pdf_comments.py
```

The script will:
1. Download the PDF from Google Drive
2. Extract all comments, annotations, and highlighted text
3. Save results to:
   - `pdf_comments.txt` - Human-readable format
   - `pdf_comments.json` - JSON format for programmatic access

## Output

The script extracts:
- Comment text
- Author information
- Page numbers
- Highlighted/annotated text
- Comment types (highlight, note, etc.)
- Creation/modification dates
