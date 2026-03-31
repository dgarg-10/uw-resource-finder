function ResourceModal({ resource, hours, onClose }) {
    if (!resource) return null;
  
    const dayOrder = [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday",
    ];
  
    const sortedHours = dayOrder.map((day) => {
      const found = hours.find((h) => h.day_of_week === day);
      return found || { day_of_week: day, is_closed: true };
    });
  
    const today = new Date().toLocaleDateString("en-US", { weekday: "long" });
  
    return (
      <div className="modal-overlay" onClick={onClose}>
        <div className="modal-content" onClick={(e) => e.stopPropagation()}>
          <button className="modal-close" onClick={onClose}>
            ✕
          </button>
          <h2 className="modal-title">{resource.name}</h2>
          <span className={`type-badge ${resource.type}`}>{resource.type}</span>
          {resource.location && (
            <p className="modal-location">📍 {resource.location}</p>
          )}
          {resource.description && (
            <p className="modal-description">{resource.description}</p>
          )}
  
          <h3 className="hours-heading">Hours</h3>
          <table className="hours-table">
            <thead>
              <tr>
                <th>Day</th>
                <th>Hours</th>
              </tr>
            </thead>
            <tbody>
              {sortedHours.map((h) => (
                <tr
                  key={h.day_of_week}
                  className={h.day_of_week === today ? "today-row" : ""}
                >
                  <td>{h.day_of_week}</td>
                  <td>
                    {h.is_closed
                      ? "Closed"
                      : `${h.open_time} – ${h.close_time}`}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    );
  }
  
  export default ResourceModal;