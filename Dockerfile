FROM python:3
RUN pip install --no-cache-dir requests-html
COPY ./ /app
ENTRYPOINT ["python", "/app/main.py"]
