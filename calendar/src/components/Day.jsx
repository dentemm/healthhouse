import * as React from 'react';

import * as moment from 'moment';

class Day extends React.Component {

  render() {
		
    const {day, today, isOtherMonth} = this.props;
  
    const disabled = isOtherMonth || day.weekday() === 0 || day.weekday() === 6 || moment().diff(day, 'days') > 0;
  
    return  (
      <div 
        className={"calendar__item text-white " + (today ? 'today ': '') + (isOtherMonth ? 'other ' : '' + (disabled ? 'inactive' : ''))}
        onClick={() => this.onClick(day, disabled)}
        data-toggle={disabled ? '' : 'modal'}
        data-target={disabled ? '' : '#calendarModal'}
      >
        <div className={`day ${today ? ' bg-dark-blue' : 'bg-primary '}`}>
          {`${day.format('D')}`}
        </div>
      </div>
      );
  }

 onClick = (day, disabled) => {
    
    if (disabled) {return;}

    this.props.selectDay(day);
    
    console.log('day clicked: ' + day.format('D'))
  }
}

export default Day;