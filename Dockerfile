FROM tensorflow/tensorflow
WORKDIR /estimator

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /

WORKDIR /neuralnet
CMD [ "python", "estimator.py"]