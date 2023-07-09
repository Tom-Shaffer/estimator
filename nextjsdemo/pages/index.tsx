import { Inter } from 'next/font/google'
import Predict from './components/predict'
import Chart from './components/chart'
import { useState, useEffect }from 'react'

const inter = Inter({ subsets: ['latin'] })
const pathToDataSetJson = 'estimator/jobs.json'


export default function Home() {
  const [jobsJson, setJobsJson] = useState([]);
  const [targetPoint, setTargetPoint] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(pathToDataSetJson);
      const data = await response.json();
      setJobsJson(data);
    }
    fetchData();
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
    <div style={{ display: 'flex' }}>
      <div className="input-container">
        <Predict setTargetPoint={setTargetPoint}/>
      </div>
      <div className="chart-container">
        <Chart examples={jobsJson} target={targetPoint}/>
      </div>
    </div>
    </main>
  )
}
