
# borrowed in part from: https://github.com/dimmg/dockselpy
FROM python:latest

RUN apt-get update && apt-get install -y \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb


# install geckodriver and firefox
# RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
#     wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
#     tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/local/bin && \
#     chmod +x /usr/local/bin/geckodriver && \
#     rm geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz

# RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
#     wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
#     tar xjf $FIREFOX_SETUP -C /opt/ && \
#     ln -s /opt/firefox/firefox /usr/bin/firefox && \
#     rm $FIREFOX_SETUP

RUN pip3 install selenium pytest

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

# create the log directory
RUN mkdir /logs

COPY /src /src

# CMD [ "pytest", "src/main.py" ]