# Build image
FROM python:3.13-bookworm AS builder

COPY --from=ghcr.io/astral-sh/uv:0.8.9 /uv /uvx /bin/

ENV APP_DIR=/var/app \
  UV_COMPILE_BYTECODE=1 \
  UV_PYTHON_DOWNLOADS=0

WORKDIR $APP_DIR

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev
# RUN uv sync --frozen --no-install-project --no-dev

# Copy application code
COPY . ./


# Final image
FROM python:3.13-slim-bookworm

ENV APP_DIR=/var/app \
  UV_PYTHON_DOWNLOADS=0 \
  UID=99 \
  GID=100
# UID 99 is nobody in unraid and GID 100 is users

WORKDIR $APP_DIR

COPY --from=builder /bin/uv /bin/uvx /bin/
COPY --from=builder --chown=${UID}:${GID} /var/app /var/app
#COPY --from=builder /var/app /var/app


CMD ["uv", "run", "--no-sync", "bot.py"]