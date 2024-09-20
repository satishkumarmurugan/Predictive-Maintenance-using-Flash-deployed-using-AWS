
import React, { useState } from 'react';
import './PlanStyle.css';

const TripForm = () => {
  const [formData, setFormData] = useState({
    destination: '',
    startDate: '',
    endDate: '',
    tripType: '',
    budget: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission
    console.log(formData);
  };

  return (
    <div className="trip-form-container">
  <h2>Plan Your Next Adventure</h2>
  <p>Get started by filling out the form below:</p>
  <form onSubmit={handleSubmit}>
    <label>
      Destination
      <input
        type="text"
        name="destination"
        placeholder="Enter your Destination"
        value={formData.destination}
        onChange={handleChange}
      />
    </label>
    <div className="date-labels">
      <label>
        Start Date
        <input
          type="date"
          name="startDate"
          value={formData.startDate}
          onChange={handleChange}
        />
      </label>
      <label>
        End Date
        <input
          type="date"
          name="endDate"
          value={formData.endDate}
          onChange={handleChange}
        />
      </label>
        </div>
        <div className="date-labels">
    <label>
      Trip Type
      <select name="tripType" value={formData.tripType} onChange={handleChange}>
        <option value="">Select Type</option>
        <option value="Adventure">Adventure</option>
        <option value="Relaxation">Relaxation</option>
        <option value="Cultural">Cultural</option>
        <option value="Nature">Nature</option>
      </select>
    </label>
    <label>
      Budget
      <input
        type="number"
        name="budget"
        placeholder="Enter in Rs."
        value={formData.budget}
        onChange={handleChange}
      />
          </label>
          </div>
    <button type="submit">Create Trip</button>
  </form>
</div>
  );
};

export default TripForm;
