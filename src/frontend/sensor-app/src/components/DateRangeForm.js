import React from 'react';

export class DateRangeForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            startDateString: '',
            endDateString: '',
        };
        this.handleDateChange = this.handleDateChange.bind(this);
        this.handleDateSubmission = this.handleDateSubmission.bind(this);
    }

    handleDateChange(event) {
        this.setState({
          [event.target.name]: event.target.value
        });
    }

    handleDateSubmission(event) {
        // alert(`StartDate: ${this.state.startDateString} and EndDate: ${this.state.endDateString}`);
        event.preventDefault();
        this.setState({
            startDateString: this.state.startDateString,
            endDateString: this.state.endDateString,
        });
    }

    render() {
        return (
            <>
                <h3>Enter date-range filters here (Format: yyyy-mm-dd)</h3>
                <form className="formDateRange" onSubmit={this.handleDateSubmission}>
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
                    <button type="submit">
                        Submit
                    </button>
                </form>
            </>
        );
    }
}