#!/usr/bin/python3
"""
This module provides a command-line utility to convert Markdown files to HTML.
It requires two command-line arguments: the input Markdown file and the output HTML file.
"""

import sys
import os

def markdown_to_html(md_file, html_file):
    """
    Converts a Markdown file to an HTML file.
    Currently, this function does not perform actual conversion.
    """
    pass

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

    # Call the conversion function (to be implemented)
    markdown_to_html(markdown_file, html_file)

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
