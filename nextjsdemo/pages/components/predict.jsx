import * as tf from '@tensorflow/tfjs'
import '@tensorflow/tfjs-backend-webgl'
import { useState, useEffect }from 'react'

const modelJSONPath = 'estimator/model.json'

export default function Predict() {
  const [buildingArea, setBuildingArea] = useState('');
  const [buildingVolume, setBuildingVolume] = useState('');
  const [deadlineMonths, setDeadlineMonths] = useState('');
  const [buildingType, setBuildingType] = useState('');
  const [efficiencyLevel, setEfficiencyLevel] = useState('');
  const [hvacType, setHvacType] = useState('');

  const [prediction, setPrediction] = useState('');
  
  async function handlePredictClick(event) {
    event.preventDefault(); // prevent form submission from refreshing the page

    const model = await tf.loadGraphModel(modelJSONPath);
    console.log(model.inputs[0].shape);  // print input shape
    const input = tf.tensor2d([
      [Number(buildingArea),
       Number(buildingVolume),
       Number(deadlineMonths),
       Number(buildingType === "industrial"),
       Number(buildingType === "commercial"),
       Number(buildingType === "residential"),
       Number(efficiencyLevel === "high"),
       Number(efficiencyLevel === "medium"),
       Number(efficiencyLevel === "low"),
       Number(hvacType === "geothermal"),
       Number(hvacType === "heat pump"),
       Number(hvacType === "forced air"),
       Number(hvacType === "boiler"),
      ]
    ])

    const output = model.predict(input)
    setPrediction(output.dataSync()[0])
  }

  return (
    <div>
      <h2>Predict construction cost</h2>
      <form onSubmit={handlePredictClick}>
      <label>
        Building area:
        <input type="number" name="building_area" value={buildingArea} onChange={e => setBuildingArea(e.target.value)} />
      </label>
      <br />
      <label>
        Building volume:
        <input type="number" name="building_volume" value={buildingVolume} onChange={e => setBuildingVolume(e.target.value)} />
      </label>
      <br />
      <label>
        Deadline months:
        <input type="number" name="deadline_months" value={deadlineMonths} onChange={e => setDeadlineMonths(e.target.value)} />
      </label>
      <br />
      <h3>Building type:</h3>
      <label>
        <input type="radio" name="building_type" value="commercial" checked={buildingType === "commercial"} onChange={() => setBuildingType("commercial")} />
        Commercial
      </label>
      <br />
      <label>
        <input type="radio" name="building_type" value="industrial" checked={buildingType === "industrial"} onChange={() => setBuildingType("industrial")} />
        Industrial
      </label>
      <br />
      <label>
        <input type="radio" name="building_type" value="residential" checked={buildingType === "residential"} onChange={() => setBuildingType("residential")} />
        Residential
      </label>
      <br />
      <h3>Efficiency level:</h3>
      <label>
        <input type="radio" name="efficiency_level" value="high" checked={efficiencyLevel === "high"} onChange={() => setEfficiencyLevel("high")} />
        High
      </label>
      <br />
      <label>
        <input type="radio" name="efficiency_level" value="medium" checked={efficiencyLevel === "medium"} onChange={() => setEfficiencyLevel("medium")} />
        Medium
      </label>
      <br />
      <label>
        <input type="radio" name="efficiency_level" value="low" checked={efficiencyLevel === "low"} onChange={() => setEfficiencyLevel("low")} />
        Low
      </label>
      <br />
      <h3>HVAC type:</h3>
      <label>
        <input type="radio" name="hvac_type" value="boiler" checked={hvacType === "boiler"} onChange={() => setHvacType("boiler")} />
        Boiler
      </label>
      <br />
      <label>
        <input type="radio" name="hvac_type" value="forced air" checked={hvacType === "forced air"} onChange={() => setHvacType("forced air")} />
        Forced air
      </label>
      <br />
      <label>
        <input type="radio" name="hvac_type" value="heat pump" checked={hvacType === "heat pump"} onChange={() => setHvacType("heat pump")} />
        Heat pump
      </label>
      <br />
      <label>
        <input type="radio" name="hvac_type" value="geothermal" checked={hvacType === "geothermal"} onChange={() => setHvacType("geothermal")} />
        Geothermal
      </label>
      <br />
      <br />
        <button type="submit">Predict cost</button>
      </form>
      {prediction && 
      <p>Predicted construction cost: ${prediction.toFixed(2)}</p>}
    </div>
  );
  
}
