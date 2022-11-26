FROM python:3.9
COPY ./app.py /app.py
RUN pip install fastapi uvicorn
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
