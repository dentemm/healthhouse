import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { Provider } from 'react-redux'; 
import configureStore from './redux/configureStore';

import Calendar from './components/CalendarWrapper';

const store = configureStore();

class App extends React.Component {
  
  render() {
    return (
      <Provider store={store}>
        <Calendar {...this.props}
        />
      </Provider>
    );
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('app')
);

module.hot.accept();