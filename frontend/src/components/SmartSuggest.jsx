import { useState } from "react";
import { getRecommendation } from "../services/api";

const DAILY_LIMIT = 3;
const USAGE_STORAGE_KEY = "smartSuggestUsage";

// Requests reset at midnight Pacific time, regardless of the user's own timezone.
function getPacificDateString() {
    return new Intl.DateTimeFormat("en-CA", {
        timeZone: "America/Los_Angeles",
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
    }).format(new Date());
}

function getRequestCount() {
    const today = getPacificDateString();
    try {
        const stored = JSON.parse(localStorage.getItem(USAGE_STORAGE_KEY));
        if (stored && stored.date === today) {
            return stored.count;
        }
    } catch {
        // ignore malformed/corrupt storage
    }
    return 0;
}

function incrementRequestCount() {
    const today = getPacificDateString();
    const count = getRequestCount() + 1;
    localStorage.setItem(USAGE_STORAGE_KEY, JSON.stringify({ date: today, count }));
    return count;
}

function SmartSuggest() {
    const [query, setQuery] = useState("");
    const [recommendation, setRecommendation] = useState("");
    const [loading, setLoading] = useState(false);
    const [isOpen, setIsOpen] = useState(false);
    const [error, setError] = useState("");
    const [requestCount, setRequestCount] = useState(() => getRequestCount());

    const remaining = Math.max(DAILY_LIMIT - requestCount, 0);
    const limitReached = remaining <= 0;

    async function handleSubmit() {
        if (!query.trim() || limitReached) return;

        setLoading(true);
        setRecommendation("");
        setError("");
        setRequestCount(incrementRequestCount());

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
            {remaining <= 1 && (
                <div className="smart-suggest-limit-warning">
                    {remaining === 1
                        ? "You have only 1 message left today. It will reset at midnight."
                        : "You have 0 messages left today. It will reset at midnight."}
                </div>
            )}
            <div className="smart-suggest-input">
                <input
                    type="text"
                    placeholder="e.g. I need a quiet study spot open late tonight"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === "Enter" && !loading) handleSubmit();
                    }}
                    disabled={loading || limitReached}
                />
                <button
                    className="suggest-btn"
                    onClick={handleSubmit}
                    disabled={loading || limitReached}
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