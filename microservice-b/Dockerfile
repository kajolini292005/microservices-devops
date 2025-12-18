FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5001

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
 CMD python -c "import requests; requests.get('http://localhost:5001/health')"

CMD ["python", "app.py"]
