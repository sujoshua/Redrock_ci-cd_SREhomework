FROM fnndsc/ubuntu-python3:ubuntu20.04-python3.8.10

MAINTAINER Joshua Su
MAINTAINER 1787548456@qq.com    


RUN mkdir /var/www
RUN cd /var/www 
ADD . .
RUN python -m pip install --upgrate pip 
RUN pip install -r requirements.txt

ENTRYPOINT uvicorn main:app 
