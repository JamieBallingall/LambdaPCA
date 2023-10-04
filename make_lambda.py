# This script will strip out any comments, spaces or newline characters from a file
# It acts a compiler for Excel LAMBDA functions, allowing us to write more structured functions
#
# Usage is of the form
#   python make_lambda.py < WIBBLE.lambda > WIBBLE.min.lambda

import sys

def clean_function(input_text):
  lines = input_text.split("\n")
  processed_lines = []

  for line in lines:
    # Remove comments (lines starting with "//")
    if "//" in line:
      line = line[:line.index("//")]
    line = line.replace(" ", "") # Remove spaces
    processed_lines.append(line)

  return "".join(processed_lines) + "\n"

if __name__ == "__main__":
  try:
    input_text = sys.stdin.read()               # Read from STDIN until EOF is encountered
    processed_text = clean_function(input_text) # Remove spaces, newlines, and comments
    sys.stdout.write(processed_text)            # Write the processed text to STDOUT

  except KeyboardInterrupt:
    sys.exit(0) # In case of KeyboardInterrupt (e.g., Ctrl+C), gracefully exit without errors
