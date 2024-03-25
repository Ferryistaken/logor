import argparse
import fnmatch
import subprocess
import pyperclip
from pathlib import Path

def get_git_tracked_files():
    """Get a list of files tracked by Git."""
    try:
        completed_process = subprocess.run(['git', 'ls-files'], check=True, capture_output=True, text=True)
        file_paths = completed_process.stdout.splitlines()
        return file_paths
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while trying to list git tracked files: {e}")
        return []

def filter_files(file_paths, includes, excludes):
    """Filter files based on include and exclude patterns."""
    filtered_files = []

    if includes:
        for pattern in includes:
            filtered_files.extend(fnmatch.filter(file_paths, pattern))
    else:
        filtered_files = file_paths

    if excludes:
        for pattern in excludes:
            filtered_files = [f for f in filtered_files if not fnmatch.fnmatch(f, pattern)]

    return list(set(filtered_files))

def read_files_content(file_paths):
    """Read and return the content of each file."""
    content = ""
    for path in file_paths:
        try:
            with open(path, 'r') as file:
                file_content = file.read()
                content += f"File: {path}\nContent:\n{file_content}\n{'-'*40}\n"
        except Exception as e:
            content += f"Error reading file {path}: {e}\n"
    return content

def main():
    parser = argparse.ArgumentParser(description="Print files from a git repo matching certain patterns.")
    parser.add_argument('-i', '--include', action='append', default=[], help='Pattern to include (can be used multiple times).')
    parser.add_argument('-e', '--exclude', action='append', default=[], help='Pattern to exclude (can be used multiple times).')
    parser.add_argument('-c', '--copy', action='store_true', help='Copy the output to the clipboard for easy pasting.')

    args = parser.parse_args()

    git_files = get_git_tracked_files()
    filtered_files = filter_files(git_files, args.include, args.exclude)
    output_content = read_files_content(filtered_files)

    if args.copy:
        pyperclip.copy(output_content)
        print("Output has been copied to the clipboard.")
    else:
        print(output_content)

if __name__ == "__main__":
    main()
