FROM python:3.11.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

LABEL maintainer="randomnaya@pochta.com"

COPY . /code
WORKDIR code
RUN pip install -r requirements.txt


EXPOSE 8000 # Строка документации. Фактически ничего не выполняет

ENTRYPOINT ["python3.11", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]