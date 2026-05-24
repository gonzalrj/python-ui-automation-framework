FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    chromium chromium-driver libnss3 libgbm1 \
    libatk-bridge2.0-0 libgtk-3-0 libasound2

# Copy and install Python dependencies separately
COPY requirements/ /tmp/requirements/
RUN pip install --break-system-packages -r /tmp/requirements/common.txt && \
    pip install --break-system-packages -r /tmp/requirements/selenium.txt && \
    pip install --break-system-packages -r /tmp/requirements/playwright.txt

# Install browsers
RUN playwright install