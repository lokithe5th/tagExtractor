import os
import argparse
import json

def load_settings_from_file(filename="settings.json"):
    """Load target extensions and tags from a JSON file."""
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data.get('targetExtensions', []), data.get('targetTags', [])

def find_lines_with_tags(directory, target_extensions, target_tags):
    """Search for lines containing target tags in files with the specified extensions within a given directory."""
    results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in target_extensions):
                with open(os.path.join(root, file), 'r', encoding="utf-8") as f:
                    lines = f.readlines()
                    for idx, line in enumerate(lines):
                        for tag in target_tags:
                            if tag in line:
                                results.append((file, idx + 1, line.strip()))
                                break

    return results

def write_to_markdown(results, output_filename="audit.md"):
    """Write results to a markdown file."""
    with open(output_filename, 'w', encoding="utf-8") as f:
        for file, line_num, line in results:
            f.write(f"**File:** {file}  \n**Line Number:** {line_num}  \n**Content:** {line}  \n\n")

def main():
    parser = argparse.ArgumentParser(description="Search files for tags defined in settings.json.")
    parser.add_argument("-p", "--path", help="Specify the root directory. If not provided, the current directory will be used.", default=".")
    args = parser.parse_args()

    target_extensions, target_tags = load_settings_from_file()
    results = find_lines_with_tags(args.path, target_extensions, target_tags)
    write_to_markdown(results)

if __name__ == "__main__":
    main()
