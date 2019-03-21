import { combineReducers } from 'redux';

import {
  FETCH_DATA
} from './actions';

const initialState = {
  test: false
};

const calendarReducer = (state = initialState, action) => {

  switch (action.type) {

    case FETCH_DATA: 

      return {
        ...state,
        test: true
      };  

    default: 
      return state;
  }
};

const rootReducer = combineReducers({
  calendar: calendarReducer,
});

export default rootReducer;