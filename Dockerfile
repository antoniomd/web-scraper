FROM python:3

RUN mkdir /pywebscraper

WORKDIR /pywebscraper

COPY requirements.txt /pywebscraper

RUN pip install -r requirements.txt

COPY . /pywebscraper

CMD [ "python", "./webscraper.py" ]