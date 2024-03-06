FROM python:3.10-alpine

WORKDIR /app
COPY challenge .
RUN pip install -r requirements.txt && adduser -D -u 1000 myuser && chown -R myuser:myuser /app
USER myuser
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
