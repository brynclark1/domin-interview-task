// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/data');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>Real-Time Data</h1>
      <table>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>Speed Over Ground (km/h)</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.timestamps}</td> {/* Display timestamp */}
              <td>{item.latitude}</td>
              <td>{item.longitude}</td>
              <td>{item.spd_over_grnd}</td> {/* Display speed over ground */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
