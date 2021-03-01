import React, { Component } from "react";
import { CSVLink } from "react-csv";
import Select from 'react-select'

const options = [
  { value: '1', label: 'Air temperature' },
  { value: '2', label: 'Relative humidity' },
  { value: '3', label: 'Dew point' },
  { value: '4', label: 'Rainfall' },
  { value: '5', label: 'Leaf wetness' },
  { value: '6', label: 'Solar radiation' },
  { value: '7', label: 'Soil temperature' },
  { value: '8', label: 'Water content' },
]

class Download extends Component {
  csvLink = React.createRef();
    state = {
        startingDate: new Date(),
        endingDate: new Date(),
        startingTime: new Date(),
        endingTime: new Date(),
        checked: false,
        values: [],
        sdata: []
    }
    onInputchange = this.onInputchange.bind(this);
    onSubmitForm = this.onSubmitForm.bind(this);  
    // onChange = this.onChange.bind(this);
    // onChangeCheckbox = this.onChangeCheckbox.bind(this);
  
  onInputchange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }
  onChangeCheckbox = e => {
    const isChecked = !this.state.checked;
    this.setState({
      checked: isChecked,
      values: isChecked ? options : this.state.values
    });
  };
  onChange = opt => {
    const allOptionsSelected = opt.length === options.length;
    this.setState({
      checked: allOptionsSelected ? true : false,
      values: opt
    });
  };

  onSubmitForm() {
    var d1 = this.state.startingDate + "-" + this.state.startingTime;
    var d2 = this.state.endingDate + "-" + this.state.endingTime;
    console.log(d1<d2);
    var errorBox = document.getElementById("error") 
    if(d1 > d2) {
      errorBox.innerHTML = "<span style='color: red;'>"+ 
                        "Please make sure the starting timestamp is before the ending timestamp.</span>" 
    }
    else if(!this.state.endingTime || !this.state.startingTime) {
      errorBox.innerHTML = "<span style='color: red;'>"+ 
                        "Please select a starting and ending time.</span>" 
    }
    else if(this.state.values.length === 0) {
      errorBox.innerHTML = "<span style='color: red;'>"+ 
                        "Please select the sensors you want values from.</span>" 
    }
    else {
        errorBox.innerHTML = "<span style='color: green;'>"+ 
                        "Request sent! Your file will be downloaded soon.</span>" 
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
                endingTime: this.state.endingTime,
                values: this.state.values
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
      
  }

  render() {
    
    return (
      <div className="download">
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
          <br></br>
          <p>Select the sensors:</p>
          <br></br>
          <Select
          isMulti
          onChange={this.onChange}
          options={options}
          value={this.state.values}
           />

          <p>
            <input
              onChange={this.onChangeCheckbox}
              type="checkbox"
              id="selectAll"
              value="selectAll"
              checked={this.state.checked}
            />
            <label for="selectAll">Select all</label>
          </p>
          <br></br>
          
          <button onClick={this.onSubmitForm}>Submit</button>
            <CSVLink
              data={this.state.sdata}
              filename="data.csv"
              className="hidden"
              ref={this.csvLink}
              target="_blank" 
            />
          <br></br>
          <span id="error"></span>
      </div>
    );
  }
}

export default Download