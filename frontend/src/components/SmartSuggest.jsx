import { useState } from "react";
import { getRecommendation } from "../services/api";

function SmartSuggest() {
    const [query, setQuery] = useState("");
    const [recommendation, setRecommendation] = useState("");
    const [loading, setLoading] = useState(false);
    const [isOpen, setIsOpen] = useState(false);

    async function handleSubmit() {
        if (!query.trim()) return;

        setLoading(true);
        setRecommendation("");

        try {
            const data = await getRecommendation(query);
            setRecommendation(data.recommendation);
        } catch (err) {
            setRecommendation("Sorry, I couldn't get a recommendation right now. Try again later.");
        }

        setLoading(false);
    }

    if (!isOpen) {
        return (
            <button
                className="smart-suggest-toggle"
                onClick={() => setIsOpen(true)}
            >
                ✨ Ask AI for a suggestion
            </button>
        );
    }

    return (
        <div className="smart-suggest">
            <div className="smart-suggest-header">
                <h3>✨ Smart Suggest</h3>
                <button
                    className="smart-suggest-close"
                    onClick={() => {
                        setIsOpen(false);
                        setRecommendation("");
                        setQuery("");
                    }}
                >
                    ✕
                </button>
            </div>
            <p className="smart-suggest-hint">
                Ask anything about campus spaces
            </p>
            <div className="smart-suggest-input">
                <input
                    type="text"
                    placeholder="e.g. I need a quiet study spot open late tonight"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") handleSubmit();
                    }}
                />
                <button
                    className="suggest-btn"
                    onClick={handleSubmit}
                    disabled={loading}
                >
                    {loading ? "..." : "Ask"}
                </button>
            </div>
            {recommendation && (
                <div className="recommendation">
                    {recommendation}
                </div>
            )}
        </div>
    );
}

export default SmartSuggest;