import { useState } from 'react';
import { TextField, Button } from '@material-ui/core';

export default function Predict() {
  const [features, setFeatures] = useState({
    feature1: '',
    feature2: '',
    feature3: '',
  });
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const res = await fetch('/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(features),
    });
    const data = await res.json();
    setPrediction(data.prediction);
  };

  return (
    <div>
        <h1>Estimator: A Construction Bidding Neural Network</h1>
        <br />
        <p>
            Estimator is a neural network trained to leverage previous work in order to make more lucrative bids based purely on data without any judgement.
        </p>
        <br />
      <form onSubmit={handleSubmit}>
        <TextField
          label="Feature 1"
          value={features.feature1}
          onChange={(event) =>
            setFeatures((prevState) => ({
              ...prevState,
              feature1: event.target.value,
            }))
          }
        />
        <TextField
          label="Feature 2"
          value={features.feature2}
          onChange={(event) =>
            setFeatures((prevState) => ({
              ...prevState,
              feature2: event.target.value,
            }))
          }
        />
        <TextField
          label="Feature 3"
          value={features.feature3}
          onChange={(event) =>
            setFeatures((prevState) => ({
              ...prevState,
              feature3: event.target.value,
            }))
          }
        />
        {/* add more input fields as needed */}
        <Button type="submit" variant="contained" color="primary">
          Predict
        </Button>
      </form>
      {prediction && <p>The predicted job estimate is: {prediction}</p>}
    </div>
  );
}
