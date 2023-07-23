import * as tf from '@tensorflow/tfjs'
import '@tensorflow/tfjs-backend-webgl'
import { useState, useEffect } from 'react'

const modelJSONPath = 'estimator/model.json'

export default function Predict({ examples, setTargetPoint }) {
  const [buildingArea, setBuildingArea] = useState('');
  const [buildingVolume, setBuildingVolume] = useState('');
  const [deadlineMonths, setDeadlineMonths] = useState('');
  const [buildingType, setBuildingType] = useState('');
  const [efficiencyLevel, setEfficiencyLevel] = useState('');
  const [hvacType, setHvacType] = useState('');
  const [isCustomRequest, setIsCustomRequest] = useState(false);

  const [presetJob, setPresetJob] = useState([]);
  const [prediction, setPrediction] = useState('');

  const handlePresetClick = async (preset) => {
    setPresetJob(preset);

    setBuildingArea(preset.buildingArea);
    setBuildingVolume(preset.buildingVolume);
    setDeadlineMonths(preset.deadlineMonths);
    setBuildingType(preset.buildingType);
    setEfficiencyLevel(preset.efficiencyLevel);
    setHvacType(preset.hvacType);
    setPrediction(''); // Reset prediction when a preset is selected
  };

  const handlePredictClick = async (event) => {
    event.preventDefault(); // prevent form submission from refreshing the page

    const model = await tf.loadGraphModel(modelJSONPath);
    console.log(model.inputs[0].shape); // print input shape
    const input = tf.tensor2d([
      [
        Number(buildingArea),
        Number(buildingVolume),
        Number(deadlineMonths),
        Number(buildingType === 'industrial'),
        Number(buildingType === 'commercial'),
        Number(buildingType === 'residential'),
        Number(efficiencyLevel === 'high'),
        Number(efficiencyLevel === 'medium'),
        Number(efficiencyLevel === 'low'),
        Number(hvacType === 'geothermal'),
        Number(hvacType === 'heat pump'),
        Number(hvacType === 'forced air'),
        Number(hvacType === 'boiler'),
      ],
    ]);

    console.log(buildingArea);
    console.log(buildingVolume);
    console.log(deadlineMonths);
    console.log(buildingType);
    console.log(efficiencyLevel);
    console.log(hvacType);

    // Calculate the predicted cost of the inputted project
    const output = model.predict(input);
    const predictedCost = output.dataSync()[0];

    // Update the prediction state
    setPrediction(predictedCost);

    // Update the target point state
    const targetPoint = { x: Number(buildingArea), y: Number(predictedCost), building_type: buildingType };
    setTargetPoint(targetPoint);
  };

  // Randomly select 2 jobs for each category as presets
  const presetProjects = [];
  const residentialPresets = getRandomPresets(examples, 2, 'building.residential');
  const commercialPresets = getRandomPresets(examples, 2, 'building.commercial');
  const industrialPresets = getRandomPresets(examples, 2, 'building.industrial');
  if (Array.isArray(residentialPresets))
    presetProjects.push(...residentialPresets);
  if (Array.isArray(commercialPresets))
    presetProjects.push(...commercialPresets);
  if (Array.isArray(industrialPresets))
    presetProjects.push(...industrialPresets);

  function getRandomPresets(jobs, count, category) {
    const shuffled = jobs
      ?.filter((job) => job.building_type === category)
      ?.sort(() => 0.5 - Math.random());
    return shuffled?.slice(0, count).map((job, index) => ({
      label: `random ${category.replace('building.', '')} job ${index + 1}`,
      actualCost: job.budget,
      buildingArea: job.building_area,
      buildingVolume: job.building_volume,
      deadlineMonths: job.deadline_months,
      buildingType: job.building_type.replace('building.', ''),
      efficiencyLevel: job.efficiency_level,
      hvacType: job.hvac_type,
    }));
  }

  const handleToggleChange = (event) => {
    setIsCustomRequest(event.target.checked);
    setBuildingArea('');
    setBuildingVolume('');
    setDeadlineMonths('');
    setBuildingType('');
    setEfficiencyLevel('');
    setHvacType('');
    setPresetJob([]);
  };

  return (
    <div>
      <h2>Predict construction cost</h2>
      <div>
        <label>
          <input
            type="checkbox"
            checked={isCustomRequest}
            onChange={handleToggleChange}
          />
          Custom Request
        </label>
      </div>
      {isCustomRequest ? (
        <form onSubmit={handlePredictClick}>
          <label>
            Building area:
            <input
              type="number"
              name="building_area"
              value={buildingArea}
              onChange={(e) => setBuildingArea(e.target.value)}
            />
          </label>
          <br />
          <label>
            Building volume:
            <input
              type="number"
              name="building_volume"
              value={buildingVolume}
              onChange={(e) => setBuildingVolume(e.target.value)}
            />
          </label>
          <br />
          <label>
            Deadline months:
            <input
              type="number"
              name="deadline_months"
              value={deadlineMonths}
              onChange={(e) => setDeadlineMonths(e.target.value)}
            />
          </label>
          <br />
          <h3>Building type:</h3>
          <label>
            <input
              type="radio"
              name="building_type"
              value="commercial"
              checked={buildingType === 'commercial'}
              onChange={() => setBuildingType('commercial')}
            />
            Commercial
          </label>
          <br />
          <label>
            <input
              type="radio"
              name="building_type"
              value="industrial"
              checked={buildingType === 'industrial'}
              onChange={() => setBuildingType('industrial')}
            />
            Industrial
          </label>
          <br />
          <label>
            <input
              type="radio"
              name="building_type"
              value="residential"
              checked={buildingType === 'residential'}
              onChange={() => setBuildingType('residential')}
            />
            Residential
          </label>
          <br />
          <h3>Efficiency level:</h3>
          <label>
            <input
              type="radio"
              name="efficiency_level"
              value="high"
              checked={efficiencyLevel === 'efficiency.high'}
              onChange={() => setEfficiencyLevel('efficiency.high')}
            />
            High
          </label>
          <br />
          <label>
            <input
              type="radio"
              name="efficiency_level"
              value="medium"
              checked={efficiencyLevel === 'efficiency.medium'}
              onChange={() => setEfficiencyLevel('efficiency.medium')}
            />
            Medium
          </label>
          <br />
          <label>
            <input
              type="radio"
              name="efficiency_level"
              value="low"
              checked={efficiencyLevel === 'efficiency.low'}
              onChange={() => setEfficiencyLevel('efficiency.low')}
            />
            Low
          </label>
          <br />
          <h3>HVAC type:</h3>
          <label>
            <input
              type="radio"
              name="hvac_type"
              value="boiler"
              checked={hvacType === 'hvac.boiler'}
              onChange={() => setHvacType('hvac.boiler')}
            />
            Boiler
          </label>
          <br />
          <label>
            <input
              type="radio"
              name="hvac_type"
              value="forced air"
              checked={hvacType === 'hvac.forcedair'}
              onChange={() => setHvacType('hvac.forcedair')}
            />
            Forced air
          </label>
          <br />
          <label>
            <input
              type="radio"
              name="hvac_type"
              value="heat pump"
              checked={hvacType === 'hvac.heatpump'}
              onChange={() => setHvacType('hvac.heatpump')}
            />
            Heat pump
          </label>
          <br />
          <label>
            <input
              type="radio"
              name="hvac_type"
              value="geothermal"
              checked={hvacType === 'hvac.geothermal'}
              onChange={() => setHvacType('hvac.geothermal')}
            />
            Geothermal
          </label>
          <br />
          <br />
        </form>
      ) : (
        <div>
          <p>Here are some example projects based on data generated:</p>
          {presetProjects.map((preset) => (
            <div key={preset.label}>
              <label>
                <input
                  type="radio"
                  name="preset_project"
                  value={preset.label}
                  checked={presetJob.label === preset.label}
                  onChange={() => handlePresetClick(preset)}
                />
                {preset.label}
              </label>
              <br />
            </div>
          ))}
        </div>
      )}
      <button onClick={handlePredictClick}>Predict</button>
      {prediction && (
        <p>MODEL Predicts construction cost: ${prediction.toFixed(0)}</p>
      )}
      {presetJob.actualCost && (
        <div>
          <p>ACTUAL construction cost: ${presetJob.actualCost}</p>
          {prediction && (
            <p>
              Percentage Error: {((prediction - presetJob.actualCost) / presetJob.actualCost * 100).toFixed(2)}%
            </p>
          )}
        </div>
      )}
    </div>
  );
}
