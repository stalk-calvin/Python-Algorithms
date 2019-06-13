# Modified from https://github.com/cclauss/Python2-and-Python3-in-Docker for python algorithms
FROM python:3.6.0-alpine as build

ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF
ENV PYTHON_VERSION 3.6

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 9.0.1

RUN set -ex \
	&& apk update \
	&& apk upgrade \
	&& apk add bash bash-completion vim wget curl \
	&& apk add --no-cache --virtual .fetch-deps \
		gnupg \
		openssl \
		tar \
		xz \
	\
	&& apk add --no-cache --virtual .build-deps  \
		bzip2-dev \
		gcc \
		gdbm-dev \
		libc-dev \
		linux-headers \
		make \
		ncurses-dev \
		openssl \
		openssl-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		zlib-dev \
	&& apk del .fetch-deps \
	&& rm -rf ~/.cache

ENV HOME /python-algorithms

RUN mkdir $HOME

WORKDIR $HOME

FROM build as test

COPY requirements.txt $HOME

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python", "run_tests.py"]
