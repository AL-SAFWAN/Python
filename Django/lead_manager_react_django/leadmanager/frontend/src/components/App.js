import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import Header from './layout/Header'
import Dashboard from './leads/Dashboard'
class App extends Component {
    render() {
        return <>
            <Header />
            <hr></hr>
            < div className="container">
                <Dashboard />
            </div>

        </>
    }
}

ReactDOM.render(
    <App />, document.getElementById('app')
)