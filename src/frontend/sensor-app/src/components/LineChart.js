import React from 'react';
import { Line } from 'react-chartjs-2';
import { filterRecordsByDate, getDatetimesArray, getReadingsArray } from './utils';
import SensorRecords from '../data/sensorRecordsSnapshot.json';

export function LineChart({ startDateString='', endDateString='' }) {
    const SensorRecordsToShow = filterRecordsByDate(SensorRecords, startDateString, endDateString);
    const data = {
        labels: getDatetimesArray(SensorRecordsToShow),
        datasets: [
            {
                label: 'Temperature readings over time',
                data: getReadingsArray(SensorRecordsToShow),
                borderColor: '#238DD8',
                fill: true,
            }
        ]
    }

    return (
        <>
            <Line data={data}
                  options={
                      {
                        title: {
                            display: true,
                            text: 'Temperature readings over time',
                            fontSize: 32,
                        },
                        scales: {
                            yAxes: [{
                              scaleLabel: {
                                display: true,
                                labelString: 'Temperature readings',
                                fontSize: 20,
                              }
                            }],
                            xAxes: [{
                              scaleLabel: {
                                display: true,
                                labelString: 'Datetime',
                                fontSize: 20,
                              }
                            }],
                        }
                      }
                  }
            />
        </>
    )
}