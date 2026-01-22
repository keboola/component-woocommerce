FROM python:3.12-slim

WORKDIR /code/

RUN pip install --upgrade pip

COPY pyproject.toml .

RUN pip install .

COPY src/ src/
COPY tests/ tests/
COPY scripts/ scripts/
COPY flake8.cfg .
COPY deploy.sh .

CMD ["python", "-u", "/code/src/component.py"]
