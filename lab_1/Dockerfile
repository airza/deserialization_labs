FROM python:3.11-slim
WORKDIR /app
RUN useradd -m appuser
COPY . /app
RUN chown -R appuser:appuser /app
RUN pip install flask
RUN echo "ARZ_$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 16)" > /app/flag.txt
EXPOSE 7777
USER appuser
CMD ["python", "app.py"]