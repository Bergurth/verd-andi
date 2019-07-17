FROM python:3

WORKDIR verd_andi

ENV DEBUG=False DB=ppp_db

ADD requirements.txt src/ /

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh .
RUN ["chmod", "+x", "entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "--bind","0.0.0.0","verd_andi.wsgi"]
