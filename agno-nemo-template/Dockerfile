FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    bash \
    gcc \
    g++ \
    make \
    python3-dev \
    git \
    nodejs \
    npm \
    ca-certificates \
    build-essential \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . .

# Create and activate virtualenv
RUN python3 -m venv .venv

# Add virtual environment to PATH
ENV PATH="/usr/src/app/.venv/bin:$PATH"

# Install using make install (handles agno conflict automatically)
RUN pip install --no-cache-dir --upgrade pip && \
    make install

# Run the xpander handler
CMD ["python", "xpander_handler.py"]
