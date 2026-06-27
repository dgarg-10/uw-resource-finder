import { useState } from "react";
import { getRecommendation } from "../services/api";

function SmartSuggest() {
    const [query, setQuery] = useState("");
    const [recommendation, setRecommendation] = useState("");
    const [loading, setLoading] = useState(false);
    const [isOpen, setIsOpen] = useState(false);
    const [error, setError] = useState("");

    async function handleSubmit() {
        if (!query.trim()) return;

        setLoading(true);
        setRecommendation("");
        setError("");

        try {
            const data = await getRecommendation(query);
            setRecommendation(data.recommendation);
        } catch (err) {
            if (err.message === "TIMEOUT") {
                setError("The request took too long. The AI service might be busy — try again in a moment.");
            } else if (err.message === "RATE_LIMITED") {
                setError("You've made too many requests. Please wait a minute before trying again.");
            } else {
                setError("Something went wrong. The AI service might be temporarily unavailable.");
            }
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
                        setError("");
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
                        if (e.key === "Enter" && !loading) handleSubmit();
                    }}
                    disabled={loading}
                />
                <button
                    className="suggest-btn"
                    onClick={handleSubmit}
                    disabled={loading}
                >
                    {loading ? "Thinking..." : "Ask"}
                </button>
            </div>
            {loading && (
                <div className="smart-suggest-loading">
                    Finding the best spots for you...
                </div>
            )}
            {error && (
                <div className="smart-suggest-error">
                    {error}
                </div>
            )}
            {recommendation && (
                <div className="recommendation">
                    {recommendation}
                </div>
            )}
        </div>
    );
}

export default SmartSuggest;