FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
COPY service-info.py .
EXPOSE 5001
CMD ["python", "service-info.py"]