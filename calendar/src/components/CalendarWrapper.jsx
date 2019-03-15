import * as React from 'react';
import * as moment from 'moment';

import CalendarHeader from './CalendarHeader';
import CalendarDays from './CalendarDays';
import Modal from './Modal';

import {month} from './../utils/calendarUtils';

class CalendarWrapper extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      currentMonth: moment(),
      visibleDays: month(moment()),
      selectedDay: undefined
    };
  }

  render() {
    return (
      <div className="calendar">
        <CalendarHeader
          month={this.state.currentMonth}
          updateMonth={this.updateMonth}
        />
        <CalendarDays
          month={this.state.currentMonth}
          days={this.state.visibleDays}
          selectDay={this.selectDay}
        />
        <Modal
          day={this.state.selectedDay}
        />
      </div>
    );
  }

  selectDay = (day) => {
    this.setState({selectedDay: day})
  }

  updateMonth = (by) => {
    const newMonth = this.state.currentMonth.clone().add(by, 'M');

    this.setState({
      currentMonth: newMonth,
      visibleDays: month(newMonth)
    });
  }
}

 export default CalendarWrapper;