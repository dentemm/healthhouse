import * as React from 'react';
import * as ReactDOM from 'react-dom';

import Calendar from './components/CalendarWrapper';

class App extends React.Component {
  
  render() {
    return <Calendar test={'tim'} />
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('app')
);

module.hot.accept();