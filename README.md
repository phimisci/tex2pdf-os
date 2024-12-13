# TEX2PDF-OS
TEX2PDF-OS is a tool for converting LaTeX files into PDF files. It is based on a texlive image and uses xelatex to perform the conversion. The container is integrated into the Magic Manuscript Maker workflow to address layout issues that arise when converting Markdown to PDF using Pandoc. In adherence to the single-source publishing principle, the TEX2PDF-OS container should only be used when layout problems can only be resolved directly in the TeX file.

## Usage
You can either start the container locally or fetch the image from GitHub Container Registry.

### Local Container
After cloning the repository, you can build the container via `docker build -t tex2pdf-os .` and start it via `docker run --rm -v $(pwd):/app/output -v $(pwd)/<FILE>.tex:/app/<FILE>.tex -v $(pwd)/images:/app/article TEX2PDF <FILE>.tex`.

1. The `<FILE>.tex` needs to be placed in the container's app folder via `-v $(pwd):<FILE>.tex:/app/<FILE>.tex`. The file name must also be provided as the last argument.
2. You need to map the output directory to the current folder `-v $(pwd):/app/output` to receive the PDF file.
3. If the article includes files, you have to place the files in `/app/article` in the container. Assuming that all images are stored in a subfolder `/images` on your local system, you need to mount this folder via `-v $(pwd)/images:/app/article`.

### GitHub Container Registry
You can fetch the image from the GitHub Container Registry via `docker pull ghcr.io/phimisci/tex2pdf-os:latest` and start it via `docker run --rm -v $(pwd):/app/output -v $(pwd)/<FILE>.tex:/app/<FILE>.tex -v $(pwd)/images:/app/article ghcr.io/phimisci/tex2pdf-os:latest <FILE>.tex`.

## About
This application was developed by Thomas Jurczyk ([thomjur](https://github.com/thomjur) on GitHub) for the journal [Philosophy and the Mind Sciences](https://philosophymindscience.org/) as part of a project funded by the German Research Foundation (DFG).

## Versions

### 1.0.0 (06.12.2024)

- Initial release
