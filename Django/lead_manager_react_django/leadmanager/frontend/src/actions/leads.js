import axios from 'axios'
import {ADD_LEAD, DELETE_LEAD, GET_LEADS} from './type'

export const getLeads = () => (dispatch, getState) => {
    axios
      .get('/api/leads/')
      .then((res) => {
        dispatch({
          type: GET_LEADS,
          payload: res.data,
        });
      })
      .catch((err) => console.log(err));
  };

  export const deleteLead = (id) => (dispatch, getState) => {
    axios
      .delete(`/api/leads/${id}/`)
      .then((res) => {
        dispatch({
          type: DELETE_LEAD,
          payload: id,
        });
      })
      .catch((err) => console.log(err));
  };

  export const addLead = (lead) => (dispatch, getState) => {
    axios
      .post(`/api/leads/`, lead)
      .then((res) => {
        dispatch({
          type: ADD_LEAD,
          payload: res.data,
        });
      })
      .catch((err) => console.log(err));
  };