import React, { Component } from 'react';

class About extends Component {
    scroll() {
        console.log("Hi");
        document.querySelector(".bottomContainer").scrollIntoView({ behavior: 'smooth' });
    }
    render(){
        return (
            <div className="about">
                <div className="aboutContainer">
                    <div className="aboutHeader">
                        <h1>OrchardWatch</h1>
                        <h3>OrchardWatch is our vision to use remote sensors to gather environmental and visual data to better manage orchard pests and keep the trees feeling good.</h3>
                        <a data-scroll href="#full">
                            <div class="arrow" onClick={this.scroll}></div>
                        </a>
                    </div>
                    <br></br>
                    
                </div>
                <div className="bottomContainer">
                    <h1>Our Mission</h1>
                    <p>‘OrchardWatch’ is our vision to use remote sensors in an effort to gather as much environmental and visual data as possible at the UMass Orchard in Belchertown, MA.  While we, and many growers, collect weather data to help manage orchards and other crops, it is usually limited to a single site on a farm. As a result, pest management and other decisions are made based on what’s happening at that weather station. Conditions around an orchard may be quite different from that one site. For example, a block surrounded by trees may have a longer wetting period than one on the top of an open hill because it takes longer to dry. This may make a difference in terms of managing apple scab and other diseases.  Another scenario: degree days may vary significantly enough that insect development will also be slower or faster in different blocks. In general we’re asking the question, do environmental conditions vary enough from place to place that management decisions could be made targeting relatively small sections of an orchard, rather than the whole farm or large blocks?</p>
                    <br></br>
                    <p>This is basically what precision agriculture does, treating relatively small parts of a farm individually based on differences in things such as soil texture and fertility. However, much of the effort to develop precision ag methods has been focused on large agronomic crops and the large farms that grow them, rather than so-called “specialty crops”, including apples and other fruit, grown on smaller farms. We want to explore whether it’s feasible to use precision agriculture, particularly for pest management, in New England orchards.</p>
                    <br></br>
                    <h1>Our History</h1>
                    <p>In order to figure it out, we’ve installed a total of nine “weather stations” over the past eight months (September 2019 through April 2020) using Onset Computer Corporation hardware and their Hobolink software to monitor “weather” conditions across 50 acres of the UMass Orchard. (Special thanks to Jim Krupa, Research Technician, for assistance with all the installations.) We are calling this our “Weather Monitoring Grid”, a major component of a larger project, OrchardWatch. (OrchardWatch involves significant web-based communication and data collection which can be shared between researchers, growers and the public.) The Weather Monitoring Grid consists of two Onset RX3000 logging base stations dubbed “OrchardWatch-North” and “OrchardWatch-South”, plus seven Onset Hobonet Field Monitoring System “motes.” The nine sensor locations vary in terms of elevation, surrounding terrain and the type of trees, and other crops, being grown. For example, one mote is at the highest point in the orchard surrounded by newly planted trees, and another is at one of the lowest areas with mature trees surrounded on three sides by woods. </p>
                    <p>Weather data are logged every five minutes and reported to the Hobolink cloud service every 10 minutes via cellular data transmission. Future plans include installing cameras at each location to capture real time orchard phenology and sky conditions. Cameras might even be able to see pest activity as if one were actually scouting in the orchard. We will investigate machine learning and statistical analysis tools to help develop and improve upon various models such as disease, pest pressure, tree growth and health, etc. </p>
                </div>
            </div>
          );
          
    }
    
}

export default About;