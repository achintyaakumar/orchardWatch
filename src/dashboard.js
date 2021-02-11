import React, { Component } from 'react';

class Dashboard extends Component {
    setIframeSource() {
        var theSelect = document.getElementById('location');
        var theIframe = document.getElementById('myIframe');
        var theUrl;
      
        theUrl = theSelect.options[theSelect.selectedIndex].value;
        theIframe.src = theUrl;
     }
    render() {
        return (
            <div className="dashboard">
                <form id="form1" method="post">
                    <br></br>
                    <label> Select a dashboard:  <select id="location" onChange={this.setIframeSource}> 
                        <option value="">Select a value ...</option> 
                        <option value="https://dashboard.hobolink.com/public/7968/Current%20conditions%20-%20OW-S-12-25-2020%2016:32:55">Current Conditions - OW-S</option> 
                        <option value="https://dashboard.hobolink.com/public/7968/Dashboard%2006-20-2020-07-23-2020%2012:02:30">Air Temperature</option> 
                        <option value="https://dashboard.hobolink.com/public/7968/Relative%20humidity%20RH-07-24-2020%2014:24:15">Relative Humidity</option> 
                        <option value="https://dashboard.hobolink.com/public/7968/Rainfall-07-30-2020%2013:30:05">Rainfall</option> 
                        <option value="https://dashboard.hobolink.com/public/7968/wetness-07-23-2020%2019:33:38">Leaf Wetness</option> 
                        <option value="https://dashboard.hobolink.com/public/7968/Dashboard%2007-23-2020-07-23-2020%2011:41:36">Soil Water Content</option> 
                        <option value="https://dashboard.hobolink.com/public/7968/Wind%20gust%20speed%20mph-08-09-2020%2014:15:27">Wind Gust Speed</option> 
                    </select></label>
                </form>
        
                <br></br> <br></br>

                <iframe title="frame" id="myIframe" src="" frameBorder="0" marginWidth="0" marginHeight="0" width="840" height="900"></iframe>

                {/* <iframe title="1" id="1" width="840px" height="900px" src="https://dashboard.hobolink.com/public/7968/Relative%20humidity%20RH-07-24-2020%2014:24:15" ></iframe> */}
            </div>
        )
    }
}

export default Dashboard