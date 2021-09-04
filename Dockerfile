FROM python:3.8

COPY script.py /code/

CMD ["python", "/code/script.py"]
