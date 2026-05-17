FROM python:3.14.2-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 4000
CMD ["python", "./endpoints.py"]