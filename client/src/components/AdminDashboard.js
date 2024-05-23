import React, { useEffect, useState } from 'react';
import { getResults, deleteResult } from './api';

function AdminDashboard() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetchResults();
  }, []);

  const fetchResults = async () => {
    const data = await getResults();
    setResults(data);
  };

  const handleDelete = async (id) => {
    await deleteResult(id);
    fetchResults();
  };

  return (
    <div>
      <h2>Admin Dashboard</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Student Name</th>
            <th>Telugu</th>
            <th>Hindi</th>
            <th>English</th>
            <th>Maths</th>
            <th>Attendance</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {results.map(result => (
            <tr key={result.id}>
              <td>{result.id}</td>
              <td>{result.studentName}</td>
              <td>{result.telugu}</td>
              <td>{result.hindi}</td>
              <td>{result.english}</td>
              <td>{result.maths}</td>
              <td>{result.attendance}</td>
              <td>
                <button onClick={() => handleDelete(result.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AdminDashboard;

