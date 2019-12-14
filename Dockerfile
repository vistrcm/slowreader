FROM python:3
COPY ./ /app
RUN pip install --no-cache-dir requests-html
ENTRYPOINT ["python", "/app/main.py"]
