FROM ubuntu:latest

WORKDIR /lta_be_service

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3.8 python3-pip python3.8-dev

RUN pip install fastapi uvicorn
RUN pip install pymssql

EXPOSE 80

COPY *.py /lta_be_service

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]