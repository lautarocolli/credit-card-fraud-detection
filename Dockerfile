FROM python:3.12.1-slim-bookworm

# Copy uv binary from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Let uv create and manage the venv
ENV UV_PROJECT_ENVIRONMENT=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
COPY pyproject.toml uv.lock ./

# Install ONLY the api optional dependencies
RUN uv sync --locked --extra api

# Copy application code and model
COPY src/predict.py src/model.bin ./

EXPOSE 8080

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8080"]