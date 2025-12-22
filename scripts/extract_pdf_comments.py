#!/usr/bin/env python3
"""
Extract comments and annotations from a PDF on Google Drive.

This script downloads a PDF from Google Drive and extracts all comments,
annotations, and highlighted text with their associated notes.
"""

import io
import sys
import json
from typing import List, Dict, Any

try:
    import requests
    import fitz  # PyMuPDF
except ImportError as e:
    print(f"Missing required package: {e}")
    print("Install with: pip install PyMuPDF requests")
    sys.exit(1)


def download_pdf_from_gdrive(file_id: str) -> bytes:
    """
    Download a PDF from Google Drive using its file ID.

    Args:
        file_id: The Google Drive file ID

    Returns:
        PDF content as bytes
    """
    # Google Drive direct download URL
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    print(f"Downloading PDF from Google Drive (ID: {file_id})...")

    session = requests.Session()
    response = session.get(url, stream=True)

    # Handle large files that require confirmation
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            params = {'id': file_id, 'confirm': value}
            response = session.get(url, params=params, stream=True)
            break

    if response.status_code != 200:
        raise Exception(f"Failed to download PDF: HTTP {response.status_code}")

    return response.content


def extract_annotations(pdf_content: bytes) -> List[Dict[str, Any]]:
    """
    Extract all annotations and comments from a PDF.

    Args:
        pdf_content: PDF file content as bytes

    Returns:
        List of dictionaries containing annotation information
    """
    annotations = []

    # Open PDF from memory
    doc = fitz.open(stream=pdf_content, filetype="pdf")

    print(f"Processing {len(doc)} pages...")

    for page_num in range(len(doc)):
        page = doc[page_num]

        # Get all annotations on this page
        annots = page.annots()

        if annots:
            for annot in annots:
                annot_info = {
                    'page': page_num + 1,
                    'type': annot.type[1] if annot.type else 'Unknown',
                    'content': annot.info.get('content', ''),
                    'subject': annot.info.get('subject', ''),
                    'author': annot.info.get('author', ''),
                    'created': annot.info.get('creationDate', ''),
                    'modified': annot.info.get('modDate', ''),
                }

                # Get the annotation rectangle and extract nearby text
                rect = annot.rect
                if rect:
                    # Expand rectangle slightly to capture context
                    expanded_rect = fitz.Rect(
                        rect.x0 - 5, rect.y0 - 5,
                        rect.x1 + 5, rect.y1 + 5
                    )
                    highlighted_text = page.get_text("text", clip=expanded_rect).strip()
                    if highlighted_text:
                        annot_info['highlighted_text'] = highlighted_text

                # Only add annotations that have content or highlighted text
                if annot_info['content'] or annot_info.get('highlighted_text'):
                    annotations.append(annot_info)

    doc.close()

    return annotations


def format_annotations(annotations: List[Dict[str, Any]]) -> str:
    """
    Format annotations as readable text.

    Args:
        annotations: List of annotation dictionaries

    Returns:
        Formatted string
    """
    if not annotations:
        return "No comments or annotations found in the PDF."

    output = [f"Found {len(annotations)} comments/annotations:\n" + "=" * 80 + "\n"]

    for i, annot in enumerate(annotations, 1):
        output.append(f"\n[Comment {i}]")
        output.append(f"Page: {annot['page']}")
        output.append(f"Type: {annot['type']}")

        if annot.get('author'):
            output.append(f"Author: {annot['author']}")

        if annot.get('highlighted_text'):
            output.append(f"Highlighted text: {annot['highlighted_text']}")

        if annot.get('content'):
            output.append(f"Comment: {annot['content']}")

        if annot.get('subject'):
            output.append(f"Subject: {annot['subject']}")

        output.append("-" * 80)

    return "\n".join(output)


def main():
    """Main function to extract comments from the PDF."""
    # Google Drive file ID for the alignment pretraining paper
    FILE_ID = "1mg2nZFOFzKZV8yw6is4FDBCykaLSvLSh"

    try:
        # Download PDF
        pdf_content = download_pdf_from_gdrive(FILE_ID)
        print(f"Downloaded {len(pdf_content)} bytes")

        # Extract annotations
        annotations = extract_annotations(pdf_content)

        # Format and print results
        formatted_output = format_annotations(annotations)
        print("\n" + formatted_output)

        # Save to file
        output_file = "pdf_comments.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_output)
        print(f"\nComments saved to: {output_file}")

        # Also save as JSON for programmatic access
        json_file = "pdf_comments.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(annotations, f, indent=2, ensure_ascii=False)
        print(f"JSON data saved to: {json_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
