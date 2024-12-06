# TEX2PDF-OS
This is the Open Source version of the TEX2PDF container. It is used to convert a LaTeX file to a PDF files using Pandoc. The container is based on the `texlive` image and uses `pdflatex` to convert the LaTeX file to a PDF file. Since the current container and its templates are customized for Philosophy and the Mind Sciences, the container is not suitable for general use. This is also the reason why this step is currently not part of the default version of the Magic Manuscipt Maker Web Application.

## Usage
You can either start the container locally or fetch the image from GitHub Container Registry.

### Local Container
After cloning the repository, you can build the container via `docker build -t tex2pdf-os .` and start it via `docker run --rm -v $(pwd):/app/output -v $(pwd):<FILE>.tex:/app/<FILE>.tex -v $(pwd)/images:/app/article TEX2PDF <FILE>.tex`.

1. The `<FILE>.tex` needs to be placed in the container's app folder via `-v $(pwd):<FILE>.tex:/app/<FILE>.tex`. The file name must also be provided as the last argument.
2. You need to map the output directory to the current folder `-v $(pwd):/app/output` to receive the PDF file.
3. If the article includes files, you have to place the files in `/app/article` in the container. Assuming that all images are stored in a subfolder `/images` on your local system, you need to mount this folder via `-v $(pwd)/images:/app/article`.

### GitHub Container Registry
You can fetch the image from the GitHub Container Registry via `docker pull ghcr.io/phimisci/tex2pdf-os:latest` and start it via `docker run --rm -v $(pwd):/app/output -v $(pwd):<FILE>.tex:/app/<FILE>.tex -v $(pwd)/images:/app/article ghcr.io/phimisci/tex2pdf-os:latest <FILE>.tex`.

## About
This application was developed by Thomas Jurczyk (thomjur on GitHub) for the journal [Philosophy and the Mind Sciences](https://philosophymindscience.org/) as part of a project funded by the German Research Foundation (DFG).

## Versions

### 1.0.0 (06.12.2024)

- Initial release
