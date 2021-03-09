import {  CREATE_MESSAGES, GET_ERROR } from './type';

export const createMessage = (msg) => {
  return {
    type: CREATE_MESSAGES,
    payload: msg,
  };
};

export const returnErrors = (msg, status) => {
  return {
    type: GET_ERROR,
    payload: { msg, status },
  };
};