import * as React from 'react';

import {connect} from 'react-redux';

import { testAction } from '../redux/actions';

class CalendarHeader extends React.Component {

  render() {
    return (
      <div className="calendar__header">
        <div className="calendar__button">
          <button
            className="btn btn-dark-blue"
            onClick={() => this.updateMonth(-1)}
          >
            Prev
          </button>
        </div>
        <div className="calendar__title">
          <h3>{this.props.month.format('MMMM YYYY')}</h3>
        </div>      
        <div className="calendar__button">
          <button
            className="btn btn-dark-blue"
            onClick={() => this.updateMonth(1)}
          >
            Next
          </button>

        </div>
      </div>
    );
  }

  updateMonth = (by) => {
    
    this.props.testAction();
    this.props.updateMonth(by);
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    testAction: () => dispatch(testAction()),
    dispatch
  };
};

export default connect(null, mapDispatchToProps)(CalendarHeader);