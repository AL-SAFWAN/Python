import axios from 'axios'
import {createMessage} from './message'
import {ADD_LEAD, DELETE_LEAD, GET_ERROR, GET_LEADS} from './type'

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
        dispatch(createMessage({ deleteLead: 'Lead Deleted' }));
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
        dispatch(createMessage({ addLead: 'Lead Added' }));
        dispatch({
          type: ADD_LEAD,
          payload: res.data,
        });
      })
      .catch((err) =>{
        const error = {
          msg : err.response.data,
          status : err.response.status
        }
        dispatch({
          type : GET_ERROR,
          payload: error}
        )
      } );
  };