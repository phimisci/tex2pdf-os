import argparse, subprocess, os, shutil

def parse_arguments():
    parser = argparse.ArgumentParser(description='Basic py script to execute TEX2PDF transformation.')
    parser.add_argument('file', type=str, help='The filename of the TeX-file.')
    parser.add_argument("--layout", type=str, help="The layout in use")

    return parser.parse_args()

def run_xelatex():
    texlive_command = ["xelatex", "-output-directory=/app/output", file_path]
    result = subprocess.run(texlive_command, capture_output=True, text=True)
    return result

def run_latexmk():
    latexmk_command = ["latexmk", "-lualatex", "-diagnostics", 
                       "-output-directory=/app/output", 
                       file_path]
    result = subprocess.run(latexmk_command, capture_output=True, text=True)
    return result

if __name__ == "__main__":
    args = parse_arguments()

    # File path
    file_path = f"/app/{args.file}"

    # Check if file exists
    if not os.path.isfile(file_path):
        print("File does not exist. Exit.")
        exit()

    # Copy all image files form article/ folder into current folder
    source_dir = os.path.join(os.getcwd(), "article")
    destination_dir = os.getcwd()
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)

    if args.layout == "classic":
        result = run_xelatex()
        if result.returncode == 0:
            print("First XeLaTeX run started successfully")
            result = run_xelatex()
            if result.returncode == 0:
                print("Second XeLaTeX run started successfully")
            else:
                print("Error during second XeLaTeX run")
                print(result.stderr)
        else:
            print("Error during first XeLaTeX run")
            print(result.stderr)

    if args.layout == "twocolumn":
        result = run_latexmk()
        if result.returncode == 0:
            print("Latexmk ran successfully")
        else:
            print("Error during Latexmk run")
            print(result.stderr)