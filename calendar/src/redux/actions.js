export const TEST_ACTION = 'TEST_ACTION';
export const SET_TOKEN = 'SET_TOKEN';

export const testAction = () => {
  return {
    type: TEST_ACTION
  };
};

export const setToken = (token) => {
  return {
    type: SET_TOKEN,
    payload: token
  };
};

export const testThunkAction = (token) => {

  const url = 'https://graph.microsoft.com/v1.0/me/';

  const config = {
    method: 'get',
    headers: new Headers({
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    })
  };

  return (dispatch) => {
    fetch(url, config)
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
};