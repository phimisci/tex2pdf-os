FROM texlive/texlive:latest-small

# Install packages
RUN apt-get update && apt-get install -y \
    ghostscript \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create directories for fonts
RUN mkdir -p /usr/share/fonts/libertinus \
    /usr/share/fonts/libertinus-math \
    /usr/share/fonts/opensans

# Set the working directory
WORKDIR /app

RUN mkdir output
RUN mkdir article

# Copy fonts and other files
COPY fonts/libertinus/. /usr/share/fonts/libertinus/
COPY fonts/libertinus-math/. /usr/share/fonts/libertinus-math/
COPY fonts/opensans/. /usr/share/fonts/opensans/
COPY tex2pdf.py /app
COPY images /app/images
COPY tex /app/tex
COPY csl /app/csl

# Update font cache
RUN fc-cache -f -v

# Install additional TeX Live packages using tlmgr
RUN tlmgr install eso-pic quoting ragged2e lastpage wallpaper lineno footmisc 
RUN tlmgr install academicons biblatex-apa babel microtype upquote footnotehyper
RUN tlmgr install xurl bookmark

ENTRYPOINT ["python3", "/app/tex2pdf.py"]