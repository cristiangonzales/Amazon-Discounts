FROM python:3-onbuild

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install pip3 install python-amazon-simple-product-api --no-compile


COPY . .

CMD [ "python3" , "amazondiscounts.src/main/main.py"]
