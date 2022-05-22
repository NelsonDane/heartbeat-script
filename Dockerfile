# Nelson Dane Summer 2022

FROM python:3.9.12

# Install python and pip. Why doesn't the python image come with pip smh my head
RUN apt-get update && apt-get install -y \
    python3-pip \
&& rm -rf /var/lib/apt/lists/*

ADD ./requirements.txt .

RUN pip install -r requirements.txt

# Default env variables
ENV WEB_HOOK_KEY="YOUR-KEY-HERE"
ENV CHECK_INTERVAL=3600
ENV PORT=43278

# Put heart.py at the bottom so that everything else is cached
ADD ./heart.py .

CMD ["python3","heart.py"]
