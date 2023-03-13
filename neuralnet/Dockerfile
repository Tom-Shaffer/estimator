FROM tensorflow/tensorflow
WORKDIR /neuralnet

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /
CMD [ "python", "estimator.py"]