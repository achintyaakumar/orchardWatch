import React, {useState, useEffect} from 'react';

function Temp() {

const [currentTempNA, setCurrentTempNA] = useState(0);
const [currentTempSA, setCurrentTempSA] = useState(0);
const [currentRHN, setCurrentRHN] = useState(0);
const [currentRHS, setCurrentRHS] = useState(0);
const [currentTSN, setCurrentTSN] = useState(0);
const [currentTSS, setCurrentTSS] = useState(0);
const [currentLWN, setCurrentLWN] = useState(0);
const [currentLWS, setCurrentLWS] = useState(0);
const [currentDPN, setCurrentDPN] = useState(0);
const [currentDPS, setCurrentDPS] = useState(0);
const [currentRN, setCurrentRN] = useState(0);
const [currentRS, setCurrentRS] = useState(0);
const [currentSRN, setCurrentSRN] = useState(0);
const [currentSRS, setCurrentSRS] = useState(0);
const [currentWCSN, setCurrentWCSN] = useState(0);
const [currentWCSS, setCurrentWCSS] = useState(0);

useEffect(() => {
  setInterval(() => {
  fetch('/api/temp').then(res => res.json()).then(data => {
    setCurrentTempNA(data.tempN);
    setCurrentTempSA(data.tempS);
    setCurrentRHN(data.RHN);
    setCurrentRHS(data.RHS);
    setCurrentTSN(data.TSN);
    setCurrentTSS(data.TSS);
    setCurrentLWN(data.LWN);
    setCurrentLWS(data.LWS);
    setCurrentDPN(data.DPN);
    setCurrentDPS(data.DPS);
    setCurrentRN(data.RN);
    setCurrentRS(data.RS);
    setCurrentSRN(data.SRN);
    setCurrentSRS(data.SRS);
    setCurrentWCSN(data.WCSN);
    setCurrentWCSS(data.WCSS);
  });
}, 20000)
}, []);

return (
    <div className="App">
      <body className="App-body">
        <table>
          <tbody>
          <tr>
            <th>Orchard North</th>
            <th>Orchard South</th>
          </tr>
          <tr>
            <td>Air temperature: {currentTempNA}°F</td>
            <td>Air temperature: {currentTempSA}°F</td>
          </tr>
          <tr>
            <td>Soil temperature: {currentTSN}°F</td>
            <td>Soil temperature: {currentTSS}°F</td>
          </tr>
          <tr>
            <td>Dew point: {currentDPN}°F</td>
            <td>Dew point: {currentDPS}°F</td>
          </tr>
          <tr>
            <td>Relative humidity: {currentRHN}%</td>
            <td>Relative humidity: {currentRHS}%</td>
          </tr>
          <tr>
            <td>Leaf wetness: {currentLWN}%</td>
            <td>Leaf wetness: {currentLWS}%</td>
          </tr>
          <tr>
            <td>Rain: {currentRN} in</td>
            <td>Rain: {currentRS} in</td>
          </tr>
          <tr>
            <td>Solar radiation: {currentSRN} W/m²</td>
            <td>Solar radiation: {currentSRS} W/m²</td>
          </tr>
          <tr>
            <td>Water content: {currentWCSN} m³/m³</td>
            <td>Water content: {currentWCSS} m³/m³</td>
          </tr>
          </tbody>
        </table>
      </body>
    </div>
  );
}

export default Temp;