import sys
import re

def main():
    try:
        with open("lint_output.txt", "r") as f:
            lines = f.readlines()
    except Exception:
        sys.exit(0)

    for line in lines:
        if "✖" in line:
            parts = re.split(r'[:✖]', line)
            if len(parts) >= 5:
                file_name = parts[0].strip()
                line_num = parts[1].strip()
                col_num = parts[2].strip()
                # Reconstruct the message which might contain colons
                message = ":".join(parts[3:]).strip()
                print(f"::error file={file_name},line={line_num},col={col_num}::{message}")

if __name__ == "__main__":
    main()
