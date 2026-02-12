# python slim versionb
FROM python:3.9-slim
# set the working directory in the container
WORKDIR /app
# copy the requirements file into the container
COPY requirements.txt .
# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy the rest of the application code into the container
COPY . .
# expose the port that the Flask app will run on
EXPOSE 5000
# set the command to run the Flask app
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0"]