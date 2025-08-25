# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install UV
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Copy project files
COPY pyproject.toml uv.lock ./
COPY src/ ./src/
COPY README.md LICENSE ./

# Install the package
RUN uv sync --frozen

# Create a non-root user
RUN useradd --create-home --shell /bin/bash alpaca
USER alpaca
WORKDIR /home/alpaca

# Set the entrypoint to alpacasay
ENTRYPOINT ["uv", "run", "alpacasay"]

# Default command
CMD ["--safer-together"]
