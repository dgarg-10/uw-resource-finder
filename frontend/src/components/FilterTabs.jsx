import { act } from "react";

const FilterTabs = ({activeTab, onTabChange}) => {
    const tabs = [
        { id: "all", label: "All" },
        { id: "favorites", label: "★ Favorites" },
        { id: "academic", label: "Buildings" },
        { id: "dining", label: "Dining"},
        { id: "library", label: "Libraries" },
        { id: "open_now", label: "Open Now" },
        { id: "student_center", label: "Student Centers" },
      ];

    return (
        <div className="filter-tabs">
            {tabs.map((tab) => (
                <button
                    key={tab.id}
                    className={`tab-btn ${activeTab === tab.id ? "active" : ""}`}
                    onClick={() => onTabChange(tab.id)}
                >
                    {tab.label}
                </button>
            ))}
        </div>
    )
}

export default FilterTabs