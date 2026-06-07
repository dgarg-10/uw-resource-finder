import {useState, useEffect} from "react";
import FilterTabs from "./components/FilterTabs";
import ResourceCard from "./components/ResourceCard";
import ResourceModal from "./components/ResourceModal";
import SearchBar from "./components/SearchBar";
import uwphoto from "./assets/uwlogo.png"
import {
  getAllResources,
  getTodayHours,
  getResourceHours,
  getFavorites,
  addFavorite,
  removeFavorite,
  getUserId,
} from "./services/api";
import "./App.css";

function App(){
  const [resources, setResources] = useState([]);
  const [todayHours, setTodayHours] = useState({});
  const [favoriteIds, setFavoriteIds] = useState([]);
  const [activeTab, setActiveTab] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedResource, setSelectedResource] = useState(null);
  const [selectedHours, setSelectedHours] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [openNowFilter, setOpenNowFilter] = useState(false);
  const [huskyAccessFilter, setHuskyAccessFilter] = useState(false);
  const [use24Hour, setUse24Hour] = useState(() => {
    return localStorage.getItem("time_format") === "24";
  })

  function toggle24Hour() {
    const newValue = !use24Hour;
    setUse24Hour(newValue);
    localStorage.setItem("time_format", newValue ? "24" : "12")
  }

  function formatTime(timeStr) {
    if (!timeStr) return "";
    if (use24Hour) return timeStr;

    const [hours, minutes] = timeStr.split(":").map(Number);
    const period = hours >= 12 ? "PM" : "AM";
    const displayHours = hours % 12 || 12;
    return `${displayHours}:${minutes.toString().padStart(2, "0")} ${period}`;
}

  const userId = getUserId();
  useEffect(() => {
    async function loadData() {
      try {
        const [resourceData, hoursData, favData] = await Promise.all([
          getAllResources(),
          getTodayHours(),
          getFavorites(userId),
        ]);

        setResources(resourceData);

        const hoursMap = {};
        hoursData.forEach((h) => {
          hoursMap[h.resource_id] = h;
        });
        setTodayHours(hoursMap);

        setFavoriteIds(favData.map((f) => f.id));
        setLoading(false);
      } catch (err) {
        console.error("Failed to load data:", err);
        setError("Failed to load data. Is the backend running?");
        setLoading(false);
      }
    }
    loadData();
  }, []);

  async function handleToggleFavorite(resourceId) {
    try {
      if (favoriteIds.includes(resourceId)) {
        await removeFavorite(userId, resourceId);
        setFavoriteIds(favoriteIds.filter((id) => id !== resourceId));
      } else {
        await addFavorite(userId, resourceId);
        setFavoriteIds([...favoriteIds, resourceId]);
      }
    } catch (err) {
      console.error("Failed to toggle favorite:", err);
    }
  }

  async function handleCardClick(resource) {
    try {
      const hours = await getResourceHours(resource.id);
      setSelectedHours(hours);
      setSelectedResource(resource);
    } catch (err) {
      console.error("Failed to load hours:", err);
    }
  }
  function getFilteredResources() {
    let filtered = resources;

    if (activeTab === "favorites") {
        filtered = filtered.filter((r) => favoriteIds.includes(r.id));
    } else if (activeTab !== "all") {
        filtered = filtered.filter((r) => r.type === activeTab);
    }

    if (openNowFilter) {
        filtered = filtered.filter((r) => {
            const hours = todayHours[r.id];
            if (!hours || hours.is_closed) return false;

            const now = new Date();
            const [openH, openM] = hours.open_time.split(":").map(Number);
            const [closeH, closeM] = hours.close_time.split(":").map(Number);

            const openDate = new Date();
            openDate.setHours(openH, openM, 0);
            const closeDate = new Date();
            closeDate.setHours(closeH, closeM, 0);

            return now >= openDate && now < closeDate;
        });
    }

    if (huskyAccessFilter) {
        filtered = filtered.filter((r) => r.husky_access === true);
    }

    if (searchQuery) {
        filtered = filtered.filter((r) =>
            r.name.toLowerCase().includes(searchQuery.toLowerCase())
        );
    }

    return filtered;
  }

  if (loading) {
    return (
      <div className="app">
        <div className="loading-screen">
          <div className="loading">Loading campus resources, this may take a moment</div>
<<<<<<< HEAD
          <img className="loading" src={uwphoto}/>
=======
          <img className="loading" src="../uwlogo.png"/>
>>>>>>> 2547a87c8e57180959e4938673bbe3db78a70c3c
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app">
        <div className="error">{error}</div>
      </div>
    );
  }

  const filtered = getFilteredResources();

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-row">
          <div>
            <h1>UW Campus Resources</h1>
            <p className="app-subtitle">Find buildings, libraries, and hours</p>
          </div>
          <button
            className="time-toggle"
            onClick={toggle24Hour}
          >
            {use24Hour ? "24h" : "12h"}
          </button>
        </div>
      </header>

      <FilterTabs
          activeTab={activeTab}
          onTabChange={(tab) => setActiveTab(activeTab === tab ? "all" : tab)}
          openNowFilter={openNowFilter}
          onToggleOpenNow={() => setOpenNowFilter(!openNowFilter)}
          huskyAccessFilter={huskyAccessFilter}
          onToggleHuskyAccess={() => setHuskyAccessFilter(!huskyAccessFilter)}
      />
      <SearchBar value={searchQuery} onChange={setSearchQuery} />

      <div className="resource-grid">
        {filtered.length > 0 ? (
          filtered.map((resource) => (
            <ResourceCard
              key={resource.id}
              resource={resource}
              todayHours={todayHours[resource.id]}
              isFavorite={favoriteIds.includes(resource.id)}
              onToggleFavorite={handleToggleFavorite}
              onClick={() => handleCardClick(resource)}
              formatTime={formatTime}
            />
          ))
        ) : (
          <div className="empty-state">
            <p>No resources found</p>
          </div>
        )}
      </div>

      {selectedResource && (
        <ResourceModal
          resource={selectedResource}
          hours={selectedHours}
          onClose={() => setSelectedResource(null)}
          formatTime={formatTime}
        />
      )}
    </div>
  );
}

export default App;



