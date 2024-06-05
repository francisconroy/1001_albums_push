FROM python:3.12-slim
LABEL authors="francisconroy"

RUN apt update && apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

COPY albumgenerator.py config.py main.py util.py word_list.txt /app/
COPY conf/ /app/conf/

CMD ["python", "main.py"]