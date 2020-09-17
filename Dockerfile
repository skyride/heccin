FROM python:3.8

WORKDIR /app

RUN pip install --no-cache-dir uWSGI==2.0.18

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy files
COPY . /app

# Collectstatic, fake these values because they're required even though
# we don't use them.
ARG SECRET_KEY=collectstatic
RUN ./manage.py collectstatic --noinput

# Ops Parameters
ENV WORKERS=2
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

CMD uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module heccin.wsgi:application
