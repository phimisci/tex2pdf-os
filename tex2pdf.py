# Copyright (c) 2024 Thomas Jurczyk
# This software is provided under the MIT License.
# For more information, please refer to the LICENSE file in the root directory of this project.

import argparse, subprocess, os

parser = argparse.ArgumentParser(description='Basic py script to execute TEX2PDF transformation.')
parser.add_argument('file', type=str, help='The filename of the TeX-file.')

args = parser.parse_args()

# File path
file_path = f"/app/{args.file}"

# Check if file exists
if not os.path.isfile(file_path):
    print("File does not exist. Exit.")
    exit()

# Create pdf from tex
texlive_command = ["xelatex", "-output-directory=/app/output", file_path]

result = subprocess.run(texlive_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful
if result.returncode == 0:
    print("XeLaTeX started successfully")
else:
    print("Error running XeLaTeX")
    print(result.stderr)