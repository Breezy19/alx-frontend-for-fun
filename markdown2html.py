#!/usr/bin/python3
"""
This module provides a command-line utility to convert Markdown files to HTML.
It handles headings, unordered lists, paragraphs, bold, and italic text.
"""

import sys
import os
import re

def markdown_to_html(md_file, html_file):
    """
    Converts a Markdown file to an HTML file with specified features.
    """
    try:
        with open(md_file, 'r') as md, open(html_file, 'w') as html:
            in_paragraph = False  # Track whether we're in a paragraph

            for line in md:
                # Convert Markdown bold and italic syntax to HTML
                line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)

                # Handle Markdown headings
                if line.startswith('#'):
                    if in_paragraph:
                        html.write('</p>\n')
                        in_paragraph = False
                    level = line.count('#')
                    content = line.strip('# \n')
                    html.write(f"<h{level}>{content}</h{level}>\n")

                # Handle Markdown unordered lists
                elif line.startswith('- '):
                    if in_paragraph:
                        html.write('</p>\n')
                        in_paragraph = False
                    content = line.strip('- \n')
                    html.write(f"<ul>\n<li>{content}</li>\n</ul>\n")

                # Handle paragraphs
                else:
                    if not in_paragraph and line.strip():
                        html.write('<p>\n')
                        in_paragraph = True
                    if in_paragraph and line.strip():
                        html.write(f"{line.strip()}\n")
                    elif in_paragraph and not line.strip():
                        html.write('</p>\n')
                        in_paragraph = False

            # Close paragraph tag if the file ends while in a paragraph
            if in_paragraph:
                html.write('</p>\n')

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
