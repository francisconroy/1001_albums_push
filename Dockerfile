FROM python:3.12-slim
LABEL authors="francisconroy"
LABEL org.opencontainers.image.source=https://github.com/francisconroy/1001_albums_push
LABEL org.opencontainers.image.description="Simple script to push notifications for your new 1001 albums generator project"
LABEL org.opencontainers.image.licenses=MIT

RUN apt update && apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

COPY albumgenerator.py config.py main.py /app/
COPY conf/ /app/conf/

CMD ["python", "main.py"]