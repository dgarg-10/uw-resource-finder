import { act } from "react";

const FilterTabs = ({activeTab, onTabChange}) => {
    const tabs = [
        { id: "all", label: "All" },
        { id: "library", label: "Libraries" },
        { id: "academic", label: "Buildings" },
        { id: "student_center", label: "Student Centers" },
        { id: "favorites", label: "★ Favorites" },
        { id: "open_now", label: "Open Now" },
      ];

    return (
        <div className="filter-tabs">
            {tabs.map((tab) => {
                <button
                    key={tab.id}
                    className = {`tab-btn ${activeTab === tab.id ? "active" : ""}`}
                    onClick={() => onTabChange(tab.id)}
                >
                    {tab.label}
                </button>
            })}
        </div>
    )
}