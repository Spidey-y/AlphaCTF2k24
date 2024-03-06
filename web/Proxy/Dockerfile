FROM python:3.8-slim

COPY challenge/app.py /app.py
RUN pip install flask gunicorn
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
