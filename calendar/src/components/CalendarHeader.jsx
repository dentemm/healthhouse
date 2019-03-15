import * as React from 'react';

class CalendarHeader extends React.Component {

  render() {
    return (
      <div className="calendar__header">
        <div className="calendar__button">
          <button
            className="btn btn-dark-blue"
            onClick={() => this.props.updateMonth(-1)}
          >
            Prev
          </button>
        </div>
        <div className="calendar__title">
          <h4>{this.props.month.format('MMMM YYYY')}</h4>
        </div>      
        <div className="calendar__button">
          <button
            className="btn btn-dark-blue"
            onClick={() => this.props.updateMonth(1)}
          >
            Next
          </button>

        </div>
      </div>
    );
  }
}

export default CalendarHeader;