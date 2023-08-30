FROM python:3.9

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirement.txt /app/requirement.txt

WORKDIR /app

RUN pip install -r requirement.txt
RUN pip install fandogh-cli --upgrade

COPY . /app

CMD ["sh" , "run_sql.sh"]
