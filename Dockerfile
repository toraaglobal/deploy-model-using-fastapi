FROM python:3.9-slim

COPY requirements.txt .

RUN pip install -r requirements.txt && \
	rm requirements.txt

EXPOSE 80

COPY ./main.py /main.py

COPY ./models /models

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]