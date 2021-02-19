import React, { Component } from "react";
import { CSVLink } from "react-csv";

class Download extends Component {
  csvLink = React.createRef();
    state = {
        startingDate: new Date(),
        endingDate: new Date(),
        startingTime: new Date(),
        endingTime: new Date(),
        sdata: []
    }
    onInputchange = this.onInputchange.bind(this);
    onSubmitForm = this.onSubmitForm.bind(this);  
  
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
                endingDate: this.state.endingDate,
                startingTime: this.state.startingTime,
                endingTime: this.state.endingTime
              })
        }).then((response) => response.json())
        .then(data => {
          this.setState({ sdata: data }, () => {
            // click the CSVLink component to trigger the CSV download
            setTimeout(() => {
              this.csvLink.current.link.click();
           });
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
              value={this.state.sdate}
              onChange={this.onInputchange}
            />
          </label>
          <label>
            Ending date: 
            <input
              name="endingDate"
              type="date"
              value={this.state.edate}
              onChange={this.onInputchange}
            />
          </label>
          <br></br>
          <label>
            Starting time: 
            <input
              name="startingTime"
              type="time"
              value={this.state.stime}
              onChange={this.onInputchange}
            />
          </label>
          <label>
            Ending time: 
            <input
              name="endingTime"
              type="time"
              value={this.state.etime}
              onChange={this.onInputchange}
            />
          </label>
          <br></br>
          <button onClick={this.onSubmitForm}>Submit</button>
            <CSVLink
              data={this.state.sdata}
              filename="data.csv"
              className="hidden"
              ref={this.csvLink}
              target="_blank" 
            />
      </div>
    );
  }
}

export default Download