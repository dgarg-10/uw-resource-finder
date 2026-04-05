function ResourceModal({ resource, hours, onClose }) {
    if (!resource) return null;
    const directionsURL = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(resource.name + " University of Washington Seattle")}`;

    const websiteLinks = {
      "By George": "https://hfs.uw.edu/eat/locations-and-hours/by-george/",
      "Center Table": "https://hfs.uw.edu/eat/locations-and-hours/center-table/",
      "Cultivate": "https://hfs.uw.edu/eat/locations-and-hours/cultivate/",
      "Husky Den Food Court": "https://hfs.uw.edu/eat/locations-and-hours/husky-den/",
      "Local Point": "https://hfs.uw.edu/eat/locations-and-hours/local-point/",
      "Dawg Bites": "https://hfs.uw.edu/eat/locations-and-hours/dawg-bites/",
      "Husky Den Café": "https://hfs.uw.edu/eat/locations-and-hours/husky-den-cafe-the-hub/",
      "Husky Grind Café, District Market Alder": "https://hfs.uw.edu/eat/locations-and-hours/husky-grind-cafe-dm-alder/",
      "Husky Grind Café, District Market Oak": "https://hfs.uw.edu/eat/locations-and-hours/husky-grind-cafe-dm-oak/",
      "Husky Grind Café, Mercer Court": "https://hfs.uw.edu/eat/locations-and-hours/husky-grind-cafe-mercer-court/",
      "Microsoft Café": "https://hfs.uw.edu/eat/locations-and-hours/microsoft-cafe/",
      "Orin's Place": "https://hfs.uw.edu/eat/locations-and-hours/orins-place/",
      "Public Grounds": "https://hfs.uw.edu/eat/locations-and-hours/public-grounds/",
      "The Rotunda": "https://hfs.uw.edu/eat/locations-and-hours/the-rotunda/",
      "Starbucks, Population Health": "https://hfs.uw.edu/eat/locations-and-hours/starbucks-coffee-population-health/",
      "Starbucks, Suzzallo": "https://hfs.uw.edu/eat/locations-and-hours/starbucks-coffee-suzzallo/",
      "Tower Café": "https://hfs.uw.edu/eat/locations-and-hours/tower-cafe/",
      "District Market, Alder": "https://hfs.uw.edu/eat/locations-and-hours/district-market-alder/",
      "District Market, Oak": "https://hfs.uw.edu/eat/locations-and-hours/district-market-oak/",
      "Etc., The HUB": "https://hfs.uw.edu/eat/locations-and-hours/etc-the-hub/",
  };
  
  const websiteUrl = websiteLinks[resource.name] || null;

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
            <a
              className="modal-location"
              href={directionsURL}
              target="_blank"
              rel="noopener noreferrer"
              onClick={(e) => e.stopPropagation()}
            >
            📍 {resource.location} — Get Directions
            </a>
          )}

          {resource.description && (
            <p className="modal-description">{resource.description}</p>
          )}
          {websiteUrl && (
            <a
                className="modal-website"
                href={websiteUrl}
                target="_blank"
                rel="noopener noreferrer"
                onClick={(e) => e.stopPropagation()}
            >
                🍽️ View Menu & Hours
            </a>
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