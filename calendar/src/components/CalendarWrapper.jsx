import * as moment from 'moment';

import * as React from 'react';
import { connect } from 'react-redux';

import MicrosoftLogin from 'react-microsoft-login';

import { setToken } from '../redux/actions';

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
        <MicrosoftLogin
          clientId='de6c9fc9-8b94-4bcc-a0d8-1377c409a181'
          authCallback={this.authHandler}
          graphScopes={['Calendars.Read.Shared']}
        />
        <Modal
          day={this.state.selectedDay}
        />
      </div>
    );
  }

  authHandler = (err, data) => {
    console.log('auth handler');
    console.log(err, data);

    if (!err && data) {
      const token = data.accessToken;

      this.props.setToken(token);

      const getCountQuery = '$count=true';
      const contentQuery = '$select=subject,body,isCancelled,start,end,location';
      const filterQuery = `$filter=start/dateTime ge '2018-04-20T00:00'`;
      const orderByQuery = '$orderBy=start/dateTime';
      const limitByQuery = '$top=50';

      const queryString = `?${getCountQuery}&${contentQuery}&${filterQuery}&${orderByQuery}&${limitByQuery}`;

      // microsoft api: https://developer.microsoft.com/en-us/graph/graph-explorer

      console.log('going to fetch!');

      const config = {
        method: 'get',
        headers: new Headers({
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + token
        })
      }

      fetch('https://graph.microsoft.com/v1.0/me/events/' + queryString, config)
        .then(response => {

          console.log(response.status);

          return response.json();
        })
        .then(data => {
          console.log(data);
        })
        .catch(error => {
          console.log('error');
          console.log(error);
        });
    }
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

const mapDispatchToProps = (dispatch) => {
  return {
    setToken: (token) => dispatch(setToken(token)),
    dispatch
  };
};

 export default connect(null, mapDispatchToProps)(CalendarWrapper);