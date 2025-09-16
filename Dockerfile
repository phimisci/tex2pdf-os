FROM texlive/texlive:latest-full

# Install packages
RUN apt-get update && apt-get install -y \
    ghostscript \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create directories for fonts
RUN mkdir -p /usr/share/fonts/libertinus \
             /usr/share/fonts/libertinus-math \
             /usr/share/fonts/noto-sans \
             /usr/share/fonts/opensans

# Set the working directory
WORKDIR /app

RUN mkdir /app/output
RUN mkdir /app/article

# Copy fonts and other files
COPY fonts/libertinus/. /usr/share/fonts/libertinus/
COPY fonts/libertinus-math/. /usr/share/fonts/libertinus-math/
COPY fonts/opensans/. /usr/share/fonts/opensans/
COPY fonts/noto-sans/. /usr/share/fonts/noto-sans/
COPY tex2pdf.py /app
COPY images /app/images
COPY tex /app/tex
COPY csl /app/csl

# Update font cache
RUN fc-cache -f -v

RUN chmod +x /app/tex2pdf.py

ENTRYPOINT ["python3", "/app/tex2pdf.py"]
