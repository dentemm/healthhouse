import * as React from 'react';
import {connect} from 'react-redux';

import * as moment from 'moment';

import Day from './Day';

class CalendarDays extends React.Component {
	
  daysOfWeek = ['M', 'T', 'W', 'T', 'F', 'S', 'S']; 
 
  render() {
    return (
        <div className="calendar__days">
          <div className="calendar__row">
          {
            this.daysOfWeek.map((_day, index) => {
              
              return (
                <div key={`${index}`} className={"calendar__item info"}>
                    <b>{_day}</b>
                </div>
              );
            })
          }
        </div>
        <div className="calendar__row">
        {
          this.props.days.map(_day => {   

            const otherMonth = _day.month() !== this.props.month.month();
            
            return (
                <Day
                  key={_day}
                  day={_day}
                  isOtherMonth={otherMonth}
                  today={_day.isSame(moment(), 'd')}
                  selectDay={this.props.selectDay}
                />
            );
          })
        }
        </div>
      </div>
    );
  }

  componentDidUpdate() {
    console.log(this.props);
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.calendar.test,
    token: state.calendar.token
  };
};

export default connect(mapStateToProps)(CalendarDays);