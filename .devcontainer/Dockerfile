# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies for Selenium (chromium, chromedriver) and shared browser libs
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends \
    chromium chromium-driver libnss3 libgbm1 \
    libatk-bridge2.0-0 libgtk-3-0 libasound2 \
    nodejs npm \
    default-jre-headless

# Install Python dependencies
COPY requirements/ /tmp/requirements/
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --break-system-packages -r /tmp/requirements/common.txt && \
    pip install --break-system-packages -r /tmp/requirements/selenium.txt && \
    pip install --break-system-packages -r /tmp/requirements/playwright.txt

# Install Chromium only for Playwright
RUN playwright install chromium

# Install Allure CLI
RUN --mount=type=cache,target=/root/.npm \
    npm install -g allure-commandline