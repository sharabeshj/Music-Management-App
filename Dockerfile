FROM python:3.7

RUN mkdir flask

COPY . /flask/

WORKDIR /flask

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app/package_edit/change.py /usr/local/lib/python3.7/site-packages/werkzeug/__init__.py

EXPOSE 5000
