import React, { Component } from 'react'

export default class Room extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             votesToSkip:0,
             guestCanPause: false,
             isHost:false
        }
        this.roomCode =this.props.match.params.roomCode
        this.getRoomDetails()
    }

    getRoomDetails(){
        fetch(`/api/get-room?code=${this.roomCode}`).then(res => res.json())
        .then(data => {
            this.setState({
                votesToSkip: data.votes_to_skip,
                guestCanPause: data.guest_can_pause,
                isHost: data.is_host,
            })
        })
    }
    
    render() {
        return (
            <div>
                <h3> {this.roomCode}</h3>
                <p>votes :{this.state.votesToSkip}</p>
                <p>guess can pause :{this.state.guestCanPause} </p>
                <p>host :{this.state.isHost} </p>

            </div>
        )
    }
}
