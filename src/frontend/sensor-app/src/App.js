import './App.css';
import { SensorRecordsTable } from './components/SensorRecordsTable';
import { SensorLineChart } from './components/SensorLineChart';
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
      <SensorLineChart startDateString={startDateString}
                       endDateString={endDateString}
      />
      <br /><br />
    </div>
  );
}

export default App;