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
const [currentATM, setCurrentATM] = useState(0);
const [currentATE, setCurrentATE] = useState(0);
const [currentATX, setCurrentATX] = useState(0);
const [currentATG, setCurrentATG] = useState(0);
const [currentATA16, setCurrentATA16] = useState(0);
const [currentATY, setCurrentATY] = useState(0);
const [currentATA11, setCurrentATA11] = useState(0);
const [currentRHM, setCurrentRHM] = useState(0);
const [currentRHE, setCurrentRHE] = useState(0);
const [currentRHX, setCurrentRHX] = useState(0);
const [currentRHG, setCurrentRHG] = useState(0);
const [currentRHA16, setCurrentRHA16] = useState(0);
const [currentRHY, setCurrentRHY] = useState(0);
const [currentRHA11, setCurrentRHA11] = useState(0);
const [currentDPM, setCurrentDPM] = useState(0);
const [currentDPE, setCurrentDPE] = useState(0);
const [currentDPX, setCurrentDPX] = useState(0);
const [currentDPG, setCurrentDPG] = useState(0);
const [currentDPA16, setCurrentDPA16] = useState(0);
const [currentDPY, setCurrentDPY] = useState(0);
const [currentDPA11, setCurrentDPA11] = useState(0);
const [currentTSM, setCurrentTSM] = useState(0);
const [currentTSE, setCurrentTSE] = useState(0);
const [currentTSX, setCurrentTSX] = useState(0);
const [currentTSG, setCurrentTSG] = useState(0);
const [currentTSA16, setCurrentTSA16] = useState(0);
const [currentTSY, setCurrentTSY] = useState(0);
const [currentTSA11, setCurrentTSA11] = useState(0);
const [currentLWM, setCurrentLWM] = useState(0);
const [currentLWE, setCurrentLWE] = useState(0);
const [currentLWX, setCurrentLWX] = useState(0);
const [currentLWG, setCurrentLWG] = useState(0);
const [currentLWA16, setCurrentLWA16] = useState(0);
const [currentLWY, setCurrentLWY] = useState(0);
const [currentLWA11, setCurrentLWA11] = useState(0);
const [currentRM, setCurrentRM] = useState(0);
const [currentRE, setCurrentRE] = useState(0);
const [currentRX, setCurrentRX] = useState(0);
const [currentRG, setCurrentRG] = useState(0);
const [currentRA16, setCurrentRA16] = useState(0);
const [currentRY, setCurrentRY] = useState(0);
const [currentRA11, setCurrentRA11] = useState(0);
const [currentSRM, setCurrentSRM] = useState(0);
const [currentSRE, setCurrentSRE] = useState(0);
const [currentSRX, setCurrentSRX] = useState(0);
const [currentSRG, setCurrentSRG] = useState(0);
const [currentSRA16, setCurrentSRA16] = useState(0);
const [currentSRY, setCurrentSRY] = useState(0);
const [currentSRA11, setCurrentSRA11] = useState(0);
const [currentWCM, setCurrentWCM] = useState(0);
const [currentWCE, setCurrentWCE] = useState(0);
const [currentWCX, setCurrentWCX] = useState(0);
const [currentWCG, setCurrentWCG] = useState(0);
const [currentWCA16, setCurrentWCA16] = useState(0);
const [currentWCY, setCurrentWCY] = useState(0);
const [currentWCA11, setCurrentWCA11] = useState(0);
const [currentWSN, setCurrentWSN] = useState(0);
const [currentWSM, setCurrentWSM] = useState(0);
const [currentWSE, setCurrentWSE] = useState(0);
const [currentWSX, setCurrentWSX] = useState(0);
const [currentWSS, setCurrentWSS] = useState(0);
const [currentWSG, setCurrentWSG] = useState(0);
const [currentWSA16, setCurrentWSA16] = useState(0);
const [currentWSY, setCurrentWSY] = useState(0);
const [currentWSA11, setCurrentWSA11] = useState(0);
const [currentGSN, setCurrentGSN] = useState(0);
const [currentGSM, setCurrentGSM] = useState(0);
const [currentGSE, setCurrentGSE] = useState(0);
const [currentGSX, setCurrentGSX] = useState(0);
const [currentGSS, setCurrentGSS] = useState(0);
const [currentGSG, setCurrentGSG] = useState(0);
const [currentGSA16, setCurrentGSA16] = useState(0);
const [currentGSY, setCurrentGSY] = useState(0);
const [currentGSA11, setCurrentGSA11] = useState(0);
const [currentWDN, setCurrentWDN] = useState(0);
const [currentWDM, setCurrentWDM] = useState(0);
const [currentWDE, setCurrentWDE] = useState(0);
const [currentWDX, setCurrentWDX] = useState(0);
const [currentWDS, setCurrentWDS] = useState(0);
const [currentWDG, setCurrentWDG] = useState(0);
const [currentWDA16, setCurrentWDA16] = useState(0);
const [currentWDY, setCurrentWDY] = useState(0);
const [currentWDA11, setCurrentWDA11] = useState(0);
const [currentTime, setCurrentTime] = useState("Loading..");
const [ScLWN, setScLWN] = useState("Computing..");
const [ScLWM, setScLWM] = useState("Computing..");
const [ScLWE, setScLWE] = useState("Computing..");
const [ScLWX, setScLWX] = useState("Computing..");
const [ScLWS, setScLWS] = useState("Computing..");
const [ScLWG, setScLWG] = useState("Computing..");
const [ScLWA16, setScLWA16] = useState("Computing..");
const [ScLWY, setScLWY] = useState("Computing..");
const [ScLWA11, setScLWA11] = useState("Computing..");
const [ScabWarning, setScabWarning] = useState('')

useEffect(() => {
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
    setCurrentATM(data.ATM);
    setCurrentATE(data.ATE);
    setCurrentATX(data.ATX);
    setCurrentATG(data.ATG);
    setCurrentATA16(data.ATA16);
    setCurrentATY(data.ATY);
    setCurrentATA11(data.ATA11);
    setCurrentRHM(data.RHM);
    setCurrentRHE(data.RHE);
    setCurrentRHX(data.RHX);
    setCurrentRHG(data.RHG);
    setCurrentRHA16(data.RHA16);
    setCurrentRHY(data.RHY);
    setCurrentRHA11(data.RHA11);
    setCurrentDPM(data.DPM);
    setCurrentDPE(data.DPE);
    setCurrentDPX(data.DPX);
    setCurrentDPG(data.DPG);
    setCurrentDPA16(data.DPA16);
    setCurrentDPY(data.DPY);
    setCurrentDPA11(data.DPA11);
    setCurrentTSM(data.TSM);
    setCurrentTSE(data.TSE);
    setCurrentTSX(data.TSX);
    setCurrentTSG(data.TSG);
    setCurrentTSA16(data.TSA16);
    setCurrentTSY(data.TSY);
    setCurrentTSA11(data.TSA11);
    setCurrentLWM(data.LWM);
    setCurrentLWE(data.LWE);
    setCurrentLWX(data.LWX);
    setCurrentLWG(data.LWG);
    setCurrentLWA16(data.LWA16);
    setCurrentLWY(data.LWY);
    setCurrentLWA11(data.LWA11);
    setCurrentRM(data.RM);
    setCurrentRE(data.RE);
    setCurrentRX(data.RX);
    setCurrentRG(data.RG);
    setCurrentRA16(data.RA16);
    setCurrentRY(data.RY);
    setCurrentRA11(data.RA11);
    setCurrentSRM(data.SRM);
    setCurrentSRE(data.SRE);
    setCurrentSRX(data.SRX);
    setCurrentSRG(data.SRG);
    setCurrentSRA16(data.SRA16);
    setCurrentSRY(data.SRY);
    setCurrentSRA11(data.SRA11);
    setCurrentWCM(data.WCM);
    setCurrentWCE(data.WCE);
    setCurrentWCX(data.WCX);
    setCurrentWCG(data.WCG);
    setCurrentWCA16(data.WCA16);
    setCurrentWCY(data.WCY);
    setCurrentWCA11(data.WCA11);
    setCurrentWSN(data.WSN);
    setCurrentWSM(data.WSM);
    setCurrentWSE(data.WSE);
    setCurrentWSX(data.WSX);
    setCurrentWSS(data.WSS);
    setCurrentWSG(data.WSG);
    setCurrentWSA16(data.WSA16);
    setCurrentWSY(data.WSY);
    setCurrentWSA11(data.WSA11);
    setCurrentGSN(data.GSN);
    setCurrentGSM(data.GSM);
    setCurrentGSE(data.GSE);
    setCurrentGSX(data.GSX);
    setCurrentGSS(data.GSS);
    setCurrentGSG(data.GSG);
    setCurrentGSA16(data.GSA16);
    setCurrentGSY(data.GSY);
    setCurrentGSA11(data.GSA11);
    setCurrentWDN(data.WDN);
    setCurrentWDM(data.WDM);
    setCurrentWDE(data.WDE);
    setCurrentWDX(data.WDX);
    setCurrentWDS(data.WDS);
    setCurrentWDG(data.WDG);
    setCurrentWDA16(data.WDA16);
    setCurrentWDY(data.WDY);
    setCurrentWDA11(data.WDA11);
    setCurrentTime(data.data_time);
  });
}, []);

//load every 5 minutes
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
    setCurrentATM(data.ATM);
    setCurrentATE(data.ATE);
    setCurrentATX(data.ATX);
    setCurrentATG(data.ATG);
    setCurrentATA16(data.ATA16);
    setCurrentATY(data.ATY);
    setCurrentATA11(data.ATA11);
    setCurrentRHM(data.RHM);
    setCurrentRHE(data.RHE);
    setCurrentRHX(data.RHX);
    setCurrentRHG(data.RHG);
    setCurrentRHA16(data.RHA16);
    setCurrentRHY(data.RHY);
    setCurrentRHA11(data.RHA11);
    setCurrentDPM(data.DPM);
    setCurrentDPE(data.DPE);
    setCurrentDPX(data.DPX);
    setCurrentDPG(data.DPG);
    setCurrentDPA16(data.DPA16);
    setCurrentDPY(data.DPY);
    setCurrentDPA11(data.DPA11);
    setCurrentTSM(data.TSM);
    setCurrentTSE(data.TSE);
    setCurrentTSX(data.TSX);
    setCurrentTSG(data.TSG);
    setCurrentTSA16(data.TSA16);
    setCurrentTSY(data.TSY);
    setCurrentTSA11(data.TSA11);
    setCurrentLWM(data.LWM);
    setCurrentLWE(data.LWE);
    setCurrentLWX(data.LWX);
    setCurrentLWG(data.LWG);
    setCurrentLWA16(data.LWA16);
    setCurrentLWY(data.LWY);
    setCurrentLWA11(data.LWA11);
    setCurrentRM(data.RM);
    setCurrentRE(data.RE);
    setCurrentRX(data.RX);
    setCurrentRG(data.RG);
    setCurrentRA16(data.RA16);
    setCurrentRY(data.RY);
    setCurrentRA11(data.RA11);
    setCurrentSRM(data.SRM);
    setCurrentSRE(data.SRE);
    setCurrentSRX(data.SRX);
    setCurrentSRG(data.SRG);
    setCurrentSRA16(data.SRA16);
    setCurrentSRY(data.SRY);
    setCurrentSRA11(data.SRA11);
    setCurrentWCM(data.WCM);
    setCurrentWCE(data.WCE);
    setCurrentWCX(data.WCX);
    setCurrentWCG(data.WCG);
    setCurrentWCA16(data.WCA16);
    setCurrentWCY(data.WCY);
    setCurrentWCA11(data.WCA11);
    setCurrentWSN(data.WSN);
    setCurrentWSM(data.WSM);
    setCurrentWSE(data.WSE);
    setCurrentWSX(data.WSX);
    setCurrentWSS(data.WSS);
    setCurrentWSG(data.WSG);
    setCurrentWSA16(data.WSA16);
    setCurrentWSY(data.WSY);
    setCurrentWSA11(data.WSA11);
    setCurrentGSN(data.GSN);
    setCurrentGSM(data.GSM);
    setCurrentGSE(data.GSE);
    setCurrentGSX(data.GSX);
    setCurrentGSS(data.GSS);
    setCurrentGSG(data.GSG);
    setCurrentGSA16(data.GSA16);
    setCurrentGSY(data.GSY);
    setCurrentGSA11(data.GSA11);
    setCurrentWDN(data.WDN);
    setCurrentWDM(data.WDM);
    setCurrentWDE(data.WDE);
    setCurrentWDX(data.WDX);
    setCurrentWDS(data.WDS);
    setCurrentWDG(data.WDG);
    setCurrentWDA16(data.WDA16);
    setCurrentWDY(data.WDY);
    setCurrentWDA11(data.WDA11);
    setCurrentTime(data.time);
  });
}, 300000)
}, []);

useEffect(() => {
  fetch('/api/scabDB').then(res =>  res.text()).then(res => {
    setScabWarning(res);
    console.log(res)
  });
}, []);

useEffect(() => {
  fetch('/api/scab').then(res => res.json()).then(data => {
    setScLWN(data.ScLWN);
    setScLWM(data.ScLWM);
    setScLWE(data.ScLWE);
    setScLWX(data.ScLWX);
    setScLWS(data.ScLWS);
    setScLWG(data.ScLWG);
    setScLWA16(data.ScLWA16);
    setScLWY(data.ScLWY);
    setScLWA11(data.ScLWA11);
  });
}, []);

//every 15 mins
useEffect(() => {
  setInterval(() => {
  fetch('/api/scab').then(res => res.json()).then(data => {
    setScLWN(data.ScLWN);
    setScLWM(data.ScLWM);
    setScLWE(data.ScLWE);
    setScLWX(data.ScLWX);
    setScLWS(data.ScLWS);
    setScLWG(data.ScLWG);
    setScLWA16(data.ScLWA16);
    setScLWY(data.ScLWY);
    setScLWA11(data.ScLWA11);
  });
}, 900000)
}, []);

return (
    <div className="App">
      <div className="App-body">
        <p>Last update: {currentTime}</p>
        <br></br>
        <p id="error" color="red">{ScabWarning}</p>
        <br></br>
        <div align='center' hidden><img src='https://www.free-website-hit-counter.com/c.php?d=9&id=126330&s=5' border='0' alt='Free Website Hit Counter'></img><br / ><small></small></div>
        <table>
          <tbody>
          <tr>
            <th></th>
            <th>North</th>
            <th>M</th>
            <th>E</th>
            <th>X</th>
          </tr>
          <tr>
            <td>Air temperature</td>
            <td>{currentTempNA}° F</td>
            <td>{currentATM}° F</td>
            <td>{currentATE}° F</td>
            <td>{currentATX}° F</td>
          </tr>
          <tr>
            <td>Relative humidity</td>
            <td>{currentRHN}%</td>
            <td>{currentRHM}%</td>
            <td>{currentRHE}%</td>
            <td>{currentRHX}%</td>
          </tr>
          <tr>
            <td>Dew point</td>
            <td>{currentDPN}° F</td>
            <td>{currentDPM}° F</td>
            <td>{currentDPE}° F</td>
            <td>{currentDPX}° F</td>
          </tr>
          <tr>
            <td>Rainfall</td>
            <td>{currentRN} in</td>
            <td>{currentRM} in</td>
            <td>{currentRE} in</td>
            <td>{currentRX} in</td>
          </tr>
          <tr>
            <td>Leaf wetness</td>
            <td>{currentLWN}%</td>
            <td>{currentLWM}%</td>
            <td>{currentLWE}%</td>
            <td>{currentLWX}%</td>
          </tr>
          <tr>
            <td>Wind speed</td>
            <td>{currentWSN} mph</td>
            <td>{currentWSM} mph</td>
            <td>{currentWSE} mph</td>
            <td>{currentWSX} mph</td>
          </tr>
          <tr>
            <td>Gust speed</td>
            <td>{currentGSN} mph</td>
            <td>{currentGSM} mph</td>
            <td>{currentGSE} mph</td>
            <td>{currentGSX} mph</td>
          </tr>
          <tr>
            <td>Wind direction</td>
            <td>{currentWDN}°</td>
            <td>{currentWDM}°</td>
            <td>{currentWDE}°</td>
            <td>{currentWDX}°</td>
          </tr>
          <tr>
            <td>Solar radiation</td>
            <td>{currentSRN} W/m²</td>
            <td>{currentSRM} W/m²</td>
            <td>{currentSRE} W/m²</td>
            <td>{currentSRX} W/m²</td>
          </tr>
          <tr>
            <td>Soil temperature</td>
            <td>{currentTSN}° F</td>
            <td>{currentTSM}° F</td>
            <td>{currentTSE}° F</td>
            <td>{currentTSX}° F</td>
          </tr>
          <tr>
            <td>Water content</td>
            <td>{currentWCSN} m³/m³</td>
            <td>{currentWCM} m³/m³</td>
            <td>{currentWCE} m³/m³</td>
            <td>{currentWCX} m³/m³</td>
          </tr>
          <tr>
            <td>Apple Scab Risk</td>
            <td>{ScLWN}</td>
            <td>{ScLWM}</td>
            <td>{ScLWE}</td>
            <td>{ScLWX}</td>
          </tr>
          </tbody>
        </table>

        <br></br>

        <table>
          <tbody>
            <tr>
              <th></th>
              <th>South</th>
              <th>G</th>
              <th>A11</th>
              <th>Y</th>
              <th>A16</th>
            </tr>
            <tr>
            <td>Air temperature</td>
            <td>{currentTempSA}° F</td>
            <td>{currentATG}° F</td>
            <td>{currentATA16}° F</td>
            <td>{currentATY}° F</td>
            <td>{currentATA11}° F</td>
          </tr>
          <tr>
            <td>Relative humidity</td>
            <td>{currentRHS}%</td>
            <td>{currentRHG}%</td>
            <td>{currentRHA16}%</td>
            <td>{currentRHY}%</td>
            <td>{currentRHA11}%</td>
          </tr>
          <tr>
            <td>Dew point</td>
            <td>{currentDPS}° F</td>
            <td>{currentDPG}° F</td>
            <td>{currentDPA16}° F</td>
            <td>{currentDPY}° F</td>
            <td>{currentDPA11}° F</td>
          </tr>
          <tr>
            <td>Rainfall</td>
            <td>{currentRS} in</td>
            <td>{currentRG} in</td>
            <td>{currentRA16} in</td>
            <td>{currentRY} in</td>
            <td>{currentRA11} in</td>
          </tr>
          <tr>
            <td>Leaf wetness</td>
            <td>{currentLWS}%</td>
            <td>{currentLWG}%</td>
            <td>{currentLWA16}%</td>
            <td>{currentLWY}%</td>
            <td>{currentLWA11}%</td>
          </tr>
          <tr>
            <td>Wind speed</td>
            <td>{currentWSS} mph</td>
            <td>{currentWSG} mph</td>
            <td>{currentWSA16} mph</td>
            <td>{currentWSY} mph</td>
            <td>{currentWSA11} mph</td>
          </tr>
          <tr>
            <td>Gust speed</td>
            <td>{currentGSS} mph</td>
            <td>{currentGSG} mph</td>
            <td>{currentGSA16} mph</td>
            <td>{currentGSY} mph</td>
            <td>{currentGSA11} mph</td>
          </tr>
          <tr>
            <td>Wind direction</td>
            <td>{currentWDS}°</td>
            <td>{currentWDG}°</td>
            <td>{currentWDA16}°</td>
            <td>{currentWDY}°</td>
            <td>{currentWDA11}°</td>
          </tr>
          <tr>
            <td>Solar radiation</td>
            <td>{currentSRS} W/m²</td>
            <td>{currentSRG} W/m²</td>
            <td>{currentSRA16} W/m²</td>
            <td>{currentSRY} W/m²</td>
            <td>{currentSRA11} W/m²</td>
          </tr>
          <tr>
            <td>Soil temperature</td>
            <td>{currentTSS}° F</td>
            <td>{currentTSG}° F</td>
            <td>{currentTSA16}° F</td>
            <td>{currentTSY}° F</td>
            <td>{currentTSA11}° F</td>
          </tr>
          <tr>
            <td>Water content</td>
            <td>{currentWCSS} m³/m³</td>
            <td>{currentWCG} m³/m³</td>
            <td>{currentWCA16} m³/m³</td>
            <td>{currentWCY} m³/m³</td>
            <td>{currentWCA11} m³/m³</td>
          </tr>
          <tr>
            <td>Apple Scab Risk</td>
            <td>{ScLWS}</td>
            <td>{ScLWG}</td>
            <td>{ScLWA16}</td>
            <td>{ScLWY}</td>
            <td>{ScLWA11}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Temp;