import React from 'react';
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

  plugins: {
    legend: {
        onClick: () => {},
    }
}
};

export default function Chart({ examples, target }) {
  const targetDatasetLabel = target ? target.building_type : null;

  const data = {
    datasets: [
        ...(target
        ? [
            {
              label: 'Target',
              data: [{ x: target.x, y: target.y }],
              backgroundColor: 'rgba(255, 165, 0, 1)',
              pointStyle: 'triangle', // Custom point style
              pointRadius: 10, // Larger point radius
            },
          ]
        : []),
      {
        label: 'Residential Job',
        data: examples
          .filter((job) => job.building_type === 'building.residential')
          .slice(0, 500)
          .map((job) => ({ x: job.building_area, y: job.budget })),
        backgroundColor: 'rgba(255, 99, 132, 1)',
        hidden: targetDatasetLabel &&  targetDatasetLabel !== 'residential',
      },
      {
        label: 'Commercial Job',
        data: examples
          .filter((job) => job.building_type === 'building.commercial')
          .slice(0, 500)
          .map((job) => ({ x: job.building_area, y: job.budget })),
        backgroundColor: 'rgba(54, 162, 235, 1)',
        hidden: targetDatasetLabel &&  targetDatasetLabel !== 'commercial',
      },
      {
        label: 'Industrial Job',
        data: examples
          .filter((job) => job.building_type === 'building.industrial')
          .slice(0, 500)
          .map((job) => ({ x: job.building_area, y: job.budget })),
        backgroundColor: 'rgba(75, 192, 192, 1)',
        hidden: targetDatasetLabel &&  targetDatasetLabel !== 'industrial',
      },
    ],
  };

  return <Scatter options={options} data={data} />;
}