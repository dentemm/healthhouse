import * as React from 'react';
import * as ReactDOM from 'react-dom';

import {createStore, applyMiddleware} from 'redux';
import { Provider } from 'react-redux'; 
import rootReducer from './redux/reducers';

import Calendar from './components/CalendarWrapper';

const store = createStore(rootReducer)

class App extends React.Component {
  
  render() {
    return (
      <Provider store={store}>
        <Calendar
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