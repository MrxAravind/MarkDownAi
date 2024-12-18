import os
import argparse

def generate_markdown(py_files, output_file):
    """Generate a markdown file summarizing and explaining the Python files."""
    with open(output_file, 'w') as md:
        md.write("# Python Files Documentation\n")
        md.write("This document provides a structured overview of the Python files in the directory.\n\n")
        
        for py_file in py_files:
            md.write(f"## File: `{py_file}`\n")
            md.write("```python\n")
            
            with open(py_file, 'r') as f:
                code = f.read()
                md.write(code)
            
            md.write("\n````\n")
            md.write(f"### Summary\n")
            md.write(f"Provide a brief description of what `{py_file}` does.\n\n")
            md.write(f"### Explanation\n")
            md.write(f"1. Key functions or classes in `{py_file}`.\n")
            md.write(f"2. Overall logic and purpose of the code.\n\n")
        
    print(f"Markdown file created: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate a Markdown file from Python scripts.")
    parser.add_argument("directory", help="The directory containing .py files.")
    parser.add_argument("output", help="The output Markdown file.")

    args = parser.parse_args()

    # Collect all .py files in the specified directory
    py_files = [os.path.join(args.directory, f) for f in os.listdir(args.directory) if f.endswith('.py') and f !="markdown.py" ]
    if not py_files:
        print("No Python files found in the specified directory.")
        return

    # Generate the Markdown file
    generate_markdown(py_files, args.output)

if __name__ == "__main__":
    main()
