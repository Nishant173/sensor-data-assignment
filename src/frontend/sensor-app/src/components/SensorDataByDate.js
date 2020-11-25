import React from 'react';
import { SensorDataTable } from './SensorDataTable';
import { SensorDataLineChart } from './SensorDataLineChart';

export class SensorDataByDate extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            startDateString: '',
            endDateString: '',
        };
        this.handleDateChange = this.handleDateChange.bind(this);
    }

    handleDateChange(event) {
        this.setState({
          [event.target.name]: event.target.value
        });
    }

    render() {
        return (
            <>
                <h1>Sensor Information - Table and Chart</h1>
                <br />

                <h3>Enter date-range filters here (Format: yyyy-mm-dd)</h3>
                <form className="formDateRange">
                    <input type="text"
                           name="startDateString"
                           value={this.state.startDateString}
                           onChange={this.handleDateChange}
                           placeholder="Enter start-date"
                    />
                    <input type="text"
                           name="endDateString"
                           value={this.state.endDateString}
                           onChange={this.handleDateChange}
                           placeholder="Enter end-date"
                    />
                </form>

                <br /><br />
                <SensorDataLineChart startDateString={this.state.startDateString}
                                     endDateString={this.state.endDateString}
                />
                <br /><br />
                <SensorDataTable startDateString={this.state.startDateString}
                                 endDateString={this.state.endDateString}
                />
                <br /><br />
            </>
        );
    }
}