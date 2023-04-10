#start by pulling python image
FROM python

#copy requirements file into image
COPY ./requirements.txt /app/requirements.txt

#switch working directory
WORKDIR /app

#install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

#copy every content from local machine to the image

COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py"]
