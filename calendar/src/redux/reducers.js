import { combineReducers } from 'redux';

import {
  TEST_ACTION,
  SET_TOKEN
} from './actions';

const initialState = {
  test: false,
  token: ''
};

const calendarReducer = (state = initialState, action) => {

  switch (action.type) {

    case TEST_ACTION: 

      return {
        ...state,
        test: true
      };  
    
    case SET_TOKEN:

      return {
        ...state,
        token: action.payload
      }

    default: 
      return state;
  }
};

const rootReducer = combineReducers({
  calendar: calendarReducer,
});

export default rootReducer;