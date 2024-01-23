#!/usr/bin/python3
"""
This module provides a command-line utility to convert Markdown files to HTML.
It requires two command-line arguments: the input Markdown file and the output HTML file.
"""

import sys
import os
import re

def markdown_to_html(md_file, html_file):
    """
    Converts a Markdown file to an HTML file.
    This function parses Markdown headings, unordered lists, ordered lists, paragraphs, bold, and italic text, converting them to HTML.
    """
    try:
        with open(md_file, 'r') as md, open(html_file, 'w') as html:
            in_unordered_list = False  # Flag for unordered list
            in_ordered_list = False    # Flag for ordered list
            in_paragraph = False       # Flag for paragraph

            for line in md:
                # Markdown to HTML conversion for bold and italic
                line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)

                # Handle Markdown headings
                # ... [existing code for headings, lists, and paragraphs] ...
                # Add the existing code for handling headings, lists, and paragraphs here

    except IOError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function that handles command-line arguments and invokes the conversion process.
    """
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Assign arguments to variables
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Call the conversion function
    markdown_to_html(markdown_file, html_file)

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
