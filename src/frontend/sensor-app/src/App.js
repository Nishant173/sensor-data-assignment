import './App.css';
import { SensorRecordsTable } from './components/SensorRecordsTable';
import { LineChart } from './components/LineChart';
// import { DateRangeForm } from './components/DateRangeForm';

function App() {
  const startDateString = ''; // Requires 'yyyy-mm-dd' format
  const endDateString = '';
  
  return (
    <div className="App">
      <h1>Sensor Information - Table and Chart</h1>
      <SensorRecordsTable startDateString={startDateString}
                          endDateString={endDateString}
      />
      <br /><br />
      <LineChart startDateString={startDateString}
                 endDateString={endDateString}
      />
      <br /><br />
    </div>
  );
}

export default App;