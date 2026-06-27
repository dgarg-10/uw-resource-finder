# UW Campus Resource Finder

A full-stack web app that helps University of Washington students find on-campus resources, with real-time open/closed status, Husky Card access indicators, favoriting, AI-powered recommendations, and Google Maps integration.

🔗 <https://uw-resources.vercel.app/>

> Note: the backend is hosted on Render's free tier and may take ~30 seconds to wake up on the first request.

## Screenshot

<img width="864" height="864" alt="Resource-Finder" src="https://github.com/user-attachments/assets/aac7834e-85e4-499c-bdf0-87e39d39f2e4" />

## Features

- Search and Filter resources by category
- Real-time open/closed status based on current time
- Favoriting capability with persistence
- Google Map integration to display resource location
- Dining resources all have a link to their website present 
- AI-powered Smart Suggest that provides options based on your prompt

## Tech stack

- **Frontend:** React, JavaScript, Vite
- **Backend:** Flask (Python)
- **Database:** PostgreSQL via Supabase
- **Deployment:** Vercel (frontend), Render (backend)
- **AI:** Anthropic API 

## Architecture

```
React + Vite (Vercel)  →      Flask API (Render)          →  Supabase Postgres
                                ↓              ↓
                       Google Maps API   Anthropic API
```

## Running locally

```bash
# Clone the repo
git clone https://github.com//.git
cd 

# Backend setup
cd backend
pip install -r requirements.txt
flask run

# Frontend setup (in a new terminal)
cd frontend
npm install
npm run dev
```

You need to set up a database URL and an Anthropic API Key in backend/.env. You note this by writing DATABASE_URL=your_url_here, and by ANTHROPIC_API_KEY=your_key_here.


The frontend runs on `http://localhost:5173` and expects the backend on `http://localhost:5001`.


## What I learned

I learned about splitting deployment between Vercel and Render. 
Hosting the React frontend on Vercel and the Flask backend on Render meant configuring CORS on the Flask side so the deployed frontend could actually hit the API. 
Each platform handled its half well, but coordinating environment variables across two dashboards added real complexity.

I also learned about how to decide between choosing Supabase over self-hosting Postgres. 
I picked Supabase for the managed Postgres instance, hosted dashboard, and built-in auth. This creates a tradeoff, as I have a free-tier limit, but the underlying database 
is still standard Postgres if I ever need to migrate.

## Technical Decisions 

For the AI recommendations, I implemented a RAG (Retrieval-Augmented Generation) pattern rather than letting Claude answer from its training data alone. On each request, the backend retrieves all building data and current-day hours from PostgreSQL, formats it into a system prompt with the current Pacific Time, and sends it to Claude Sonnet. This grounds every recommendation in real data, so the model knows exactly what's open right now instead of guessing from potentially outdated training knowledge.

I applied different rate limits depending on the endpoint — 100 requests/minute as a default across the API, but 10 requests/minute on the `/api/recommend` endpoint specifically to control Anthropic API costs. The rate limiter returns structured JSON errors so the frontend can show the user a specific "too many requests" message rather than a generic failure.

Favorites are stored in PostgreSQL but identified by a randomly generated browser ID saved in localStorage rather than requiring user authentication. The tradeoff is that favorites don't sync across devices, but for a campus tool where most students access it from one device, avoiding a full auth system with huge overhead.