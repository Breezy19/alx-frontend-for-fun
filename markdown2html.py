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
    This function parses Markdown headings and converts them to HTML headings.
    """
    try:
        with open(md_file, 'r') as md, open(html_file, 'w') as html:
            for line in md:
                # Checking for Markdown headings
                if line.startswith('#'):
                    level = line.count('#')  # Determine the heading level
                    content = line.strip('# \n')
                    html.write(f"<h{level}>{content}</h{level}>\n")
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
