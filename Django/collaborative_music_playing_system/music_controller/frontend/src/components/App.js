import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import HomePage from './HomePage'

class App extends Component {

    constructor(props) {
        super(props)
    }

    render() {
        return (
          <div>
            <HomePage />
          </div>
        );
      }
}

ReactDOM.render(
    <App />, document.getElementById('app')
)
