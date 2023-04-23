import React from 'react';
import { useState, useEffect } from 'react'
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from 'chart.js';
import { Scatter } from 'react-chartjs-2';

const pathToDataSetJson = 'estimator/jobs.json'

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

const options = {
    scales: {
    x: {
        beginAtZero: true,
        maxPointsLimit: 100,
    },
    y: {
      beginAtZero: true,
    },
  },
};

export default function Chart({examples}) {
    const data = {
        datasets: [
            {
              label: 'Historical Jobs',
              data: examples.slice(0,100).map(job => ({x: job.building_area, y: job.budget})),
              backgroundColor: 'rgba(255, 99, 132, 1)',
            },
          ],
    }
    return <Scatter options={options} data={data} />;
}
