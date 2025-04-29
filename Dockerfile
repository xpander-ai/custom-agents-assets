# Use Alpine-based Python image
FROM python:3.12-alpine AS builder

# Set environment vars for venv
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set working directory
WORKDIR /usr/src/app

# Install base dependencies
RUN apk add --no-cache \
    bash \
    curl \
    gcc \
    g++ \
    libffi-dev \
    musl-dev \
    openssl-dev \
    make \
    python3-dev \
    rust \
    cargo \
    npm \
    wget

# Install Node.js 22 manually
RUN NODE_VERSION=22.0.0 && \
    ARCH=linux-x64 && \
    wget https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-$ARCH.tar.xz && \
    tar -xf node-v$NODE_VERSION-$ARCH.tar.xz && \
    mv node-v$NODE_VERSION-$ARCH /usr/local/node && \
    ln -s /usr/local/node/bin/node /usr/local/bin/node && \
    ln -s /usr/local/node/bin/npm /usr/local/bin/npm && \
    ln -s /usr/local/node/bin/npx /usr/local/bin/npx

# Check versions
RUN node -v && npm -v

# Create and activate virtualenv
RUN python3 -m venv $VIRTUAL_ENV

# Copy app files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Run your app
CMD ["python", "xpander_handler.py"]
