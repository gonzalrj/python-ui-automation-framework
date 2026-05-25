# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/python:3.11

ENV PYTHONUNBUFFERED=1

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends \
    libnss3 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libasound2 \
    nodejs \
    npm \
    default-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/ /tmp/requirements/

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \ 
    -r /tmp/requirements/playwright.txt \
    -r /tmp/requirements/selenium.txt

RUN playwright install chromium

RUN --mount=type=cache,target=/root/.npm \
    npm install -g allure-commandline