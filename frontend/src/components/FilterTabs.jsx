function FilterTabs({ activeTab, onTabChange, openNowFilter, onToggleOpenNow, huskyAccessFilter, onToggleHuskyAccess }) {
    const tabs = [
        { id: "all", label: "All" },
        { id: "library", label: "Libraries" },
        { id: "academic", label: "Buildings" },
        { id: "student_center", label: "Student Centers" },
        { id: "dining", label: "Dining" },
        { id: "favorites", label: "★ Favorites" },
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
            <button
                className={`tab-btn open-now-btn ${openNowFilter ? "active" : ""}`}
                onClick={onToggleOpenNow}
            >
                Open Now
            </button>
            <button
                className={`tab-btn husky-btn ${huskyAccessFilter ? "active" : ""}`}
                onClick={onToggleHuskyAccess}
            >
                🪪 Husky Access
            </button>
        </div>
    );
}

export default FilterTabs;