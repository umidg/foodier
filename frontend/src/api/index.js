/* eslint-disable */
import axios from 'axios';

const baseUrl = process.env.REACT_APP_API_URL;

//custom axios component
export const api = async (url, data, method, headers = '', params = '') => {
  const config = {
    method: method || 'GET',
    url: `${baseUrl}${url}`,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      ...headers,
    },
    data,
    params,
  };

  return axios(config);
};
