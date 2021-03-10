import { AUTH_ERROR, USER_LOADED, USER_LOADING } from '../actions/type.js'

const initialState = {
    token: localStorage.getItem('token'),
    isAuthenticated: null,
    isLoading: false,
    user: null
}


export default function (state = initialState, action) {
    switch (action.type) {

        case USER_LOADING:
            return {
                ...state,
                isLoading: true
            }

        case USER_LOADED:
            return {
                ...state, 
                isAuthenticated: true,
                isLoading: false,
                user: action.payload
            }
        case AUTH_ERROR:
            localStorage.removeItem('token')
            return {
                ...state,
                token:null,
                isAuthenticated: null,
                isLoading: false,
                user: null
            }

        default:

            return state
    }
}