function ResourceCard({
    resource,
    todayHours,
    isFavorite,
    onToggleFavorite,
    onClick,
  }) {
    function getStatusInfo() {
      if (!todayHours) {
        return { status: "unknown", label: "Hours unavailable", countdown: null };
      }
  
      if (todayHours.is_closed) {
        return { status: "closed", label: "Closed Today", countdown: null };
      }
  
      const now = new Date();
      const [openH, openM] = todayHours.open_time.split(":").map(Number);
      const [closeH, closeM] = todayHours.close_time.split(":").map(Number);
  
      const openDate = new Date();
      openDate.setHours(openH, openM, 0);
  
      const closeDate = new Date();
      closeDate.setHours(closeH, closeM, 0);
  
      if (now < openDate) {
        const diffMs = openDate - now;
        const diffH = Math.floor(diffMs / (1000 * 60 * 60));
        const diffM = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));
        const countdown =
          diffH > 0 ? `Opens in ${diffH}h ${diffM}m` : `Opens in ${diffM}m`;
        return { status: "closed", label: "Closed", countdown };
      }
  
      if (now >= closeDate) {
        return { status: "closed", label: "Closed", countdown: null };
      }
  
      const diffMs = closeDate - now;
      const diffH = Math.floor(diffMs / (1000 * 60 * 60));
      const diffM = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));
      const countdown =
        diffH > 0 ? `Closes in ${diffH}h ${diffM}m` : `Closes in ${diffM}m`;
      return { status: "open", label: "Open", countdown };
    }
  
    const { status, label, countdown } = getStatusInfo();
  
    const typeLabels = {
      library: "Library",
      academic: "Academic",
      student_center: "Student Center",
    };
  
    return (
      <div className="resource-card" onClick={onClick}>
        <div className="card-header">
          <h3 className="card-title">{resource.name}</h3>
          <button
            className={`star-btn ${isFavorite ? "active" : ""}`}
            onClick={(e) => {
              e.stopPropagation();
              onToggleFavorite(resource.id);
            }}
          >
            {isFavorite ? "★" : "☆"}
          </button>
        </div>
        <span className={`type-badge ${resource.type}`}>
          {typeLabels[resource.type] || resource.type}
        </span>
        <div className="hours-info">
          <span className={`status ${status}`}>{label}</span>
          {todayHours && !todayHours.is_closed && (
            <span className="hours-text">
              {todayHours.open_time} – {todayHours.close_time}
            </span>
          )}
        </div>
        {countdown && <span className="countdown">{countdown}</span>}
      </div>
    );
  }
  
  export default ResourceCard;