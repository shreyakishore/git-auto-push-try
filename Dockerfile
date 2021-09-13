FROM python:3
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get -y install git
#RUN git config --global credential.helper store
#RUN echo "https://shreyakishore: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@github.com" > ~/.git-credentials
#RUN git config --global user.name "shreyakishore"
#RUN git config --global user.email "shreyakishore5@gmail.com"
#RUN git config --global user.password "AnuradhaKass5"
RUN git init
RUN git remote add origin https://shreyakishore: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@github.com/shreyakishore/git-auto-push-try.git
CMD ["python", "-m", "main.__init__"]