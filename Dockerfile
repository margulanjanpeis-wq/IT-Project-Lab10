
FROM python:3.11-slim

WORKDIR /app

COPY src/ ./src/

ENV PYTHONPATH=/app

CMD ["python", "-m", "src.app"]
