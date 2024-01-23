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
    This function parses Markdown headings, unordered lists, and ordered lists, converting them to HTML.
    """
    try:
        with open(md_file, 'r') as md, open(html_file, 'w') as html:
            in_unordered_list = False  # Flag to track if we are inside an unordered list
            in_ordered_list = False    # Flag to track if we are inside an ordered list

            for line in md:
                # Handle Markdown headings
                if line.startswith('#'):
                    level = line.count('#')  # Determine the heading level
                    content = line.strip('# \n')
                    html.write(f"<h{level}>{content}</h{level}>\n")

                    # Close any open lists
                    if in_unordered_list:
                        html.write('</ul>\n')
                        in_unordered_list = False
                    if in_ordered_list:
                        html.write('</ol>\n')
                        in_ordered_list = False

                # Handle Markdown unordered lists
                elif line.startswith('- '):
                    content = line.strip('- \n')
                    if not in_unordered_list:
                        html.write('<ul>\n')
                        in_unordered_list = True
                    html.write(f"    <li>{content}</li>\n")

                    # Close ordered list if open
                    if in_ordered_list:
                        html.write('</ol>\n')
                        in_ordered_list = False

                # Handle Markdown ordered lists
                elif line.startswith('* '):
                    content = line.strip('* \n')
                    if not in_ordered_list:
                        html.write('<ol>\n')
                        in_ordered_list = True
                    html.write(f"    <li>{content}</li>\n")

                    # Close unordered list if open
                    if in_unordered_list:
                        html.write('</ul>\n')
                        in_unordered_list = False

                # Check if we are exiting a list
                elif in_unordered_list or in_ordered_list:
                    if in_unordered_list:
                        html.write('</ul>\n')
                    if in_ordered_list:
                        html.write('</ol>\n')
                    in_unordered_list = False
                    in_ordered_list = False

            # Close any open lists at the end of the file
            if in_unordered_list:
                html.write('</ul>\n')
            if in_ordered_list:
                html.write('</ol>\n')

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
