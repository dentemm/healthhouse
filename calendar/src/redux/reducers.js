import { combineReducers } from 'redux';

const initialState = {
  loading: true,
};

const calendarReducer = (state = initialState, action) => {

  switch (action.type) {

    case 'TEST': 

      return {
        ...state,
        loading: false
      };  

    default: 
      return state;
  }
};

const rootReducer = combineReducers({
  calendar: calendarReducer,
});

export default rootReducer;