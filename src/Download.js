import React, { Component } from "react";

class Download extends Component {
  constructor() {
    super();
    this.state = {
        startingDate: new Date(),
        endingDate: new Date(),
    };
    this.onInputchange = this.onInputchange.bind(this);
    this.onSubmitForm = this.onSubmitForm.bind(this);
  }

  onInputchange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  onSubmitForm() {
    console.log(this.state)
    if(this.state.endingDate > this.state.startingDate) {
        alert("Request sent!")
        fetch("/api/download", {
            method:"POST",
            cache: "no-cache",
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                startingDate: this.state.startingDate,
                endingDate: this.state.endingDate
              })
        })
    }
    else {
        alert("Ending date should be after the starting date.")
    }
      
    }

  render() {
    
    return (
      <div>
          <label>
            Starting date: 
            <input
              name="startingDate"
              type="date"
              value={this.state.fname}
              onChange={this.onInputchange}
            />
          </label>
          <label>
            Ending date: 
            <input
              name="endingDate"
              type="date"
              value={this.state.lname}
              onChange={this.onInputchange}
            />
          </label>
            <button onClick={this.onSubmitForm}>Submit</button>
      </div>
    );
  }
}

export default Download




            // <form id="downloadForm" method="post">
            //     <input type="time" name="time" value="22:00" />
            //     <br></br>
            //     <input type="date" id="date" name="date"></input>
            // </form>