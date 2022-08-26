FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y pkgconf libhdf5-dev curl linux-libc-dev && apt-get clean
RUN apt-get install --upgrade -y libgnutls30

ENV POETRY_HOME=/etc/poetry
ENV PATH="/etc/poetry/bin:$PATH"
RUN curl -sSLfo poetry-install.py https://install.python-poetry.org \
    && python poetry-install.py --version 1.1.12

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-root

COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]