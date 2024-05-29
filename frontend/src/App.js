import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);
  const [startTime, setStartTime] = useState(0);
  const [endTime, setEndTime] = useState(Date.now() / 1000); // Default to current time

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/data-range?start_time=${startTime}&end_time=${endTime}`);
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();

    // Fetch data every second
    const interval = setInterval(fetchData, 1000);

    return () => clearInterval(interval);
  }, [startTime, endTime]);

  return (
    <div className="App">
      <h1>Real-Time Data</h1>
      <label>
        Start Time:
        <input
          type="number"
          value={startTime}
          onChange={e => setStartTime(parseFloat(e.target.value))}
        />
      </label>
      <label>
        End Time:
        <input
          type="number"
          value={endTime}
          onChange={e => setEndTime(parseFloat(e.target.value))}
        />
      </label>
      <table>
        <thead>
          <tr>
            <th>Timestamps</th>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>Speed Over Ground (km/h)</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.timestamps}</td>
              <td>{item.latitude}</td>
              <td>{item.longitude}</td>
              <td>{item.spd_over_grnd}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
