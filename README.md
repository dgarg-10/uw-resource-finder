# UW Campus Resource Finder

A full-stack web app that helps University of Washington students find on-campus resources — dining halls, study spaces, gyms, and more — with real-time open/closed status, Husky Card access indicators, favoriting, and Google Maps integration.

🔗 <https://uw-resources.vercel.app/>

> Note: the backend is hosted on Render's free tier and may take ~30 seconds to wake up on the first request.

## Screenshot

<img width="864" height="864" alt="Resource-Finder" src="https://github.com/user-attachments/assets/aac7834e-85e4-499c-bdf0-87e39d39f2e4" />

## Features

- Search and Filter resources by category
- Real-time open/clsoed status based on current time
- Favoriting capability with persistence
- Google Map integration to display resource location
- Dining resources all have a link to their website present 

## Tech stack

- **Frontend:** React, TypeScript, Vite
- **Backend:** Flask (Python)
- **Database:** PostgreSQL via Supabase
- **Deployment:** Vercel (frontend), Render (backend)

## Architecture

```
React + Vite (Vercel)  →  Flask API (Render)  →  Supabase Postgres
                                ↓
                       Google Maps API
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

You need to set up a database URL in your .env for backend/.env. You note this by writing DATABASE_URL=your_url_here. 


## What I learned

I learned about splitting deployment between Vercel and Render. 
Hosting the React frontend on Vercel and the Flask backend on Render meant configuring CORS on the Flask side so the deployed frontend could actually hit the API. 
Each platform handled its half well, but coordinating environment variables across two dashboards added real complexity.

I also learned about how to decide between choosing Supabase over self-hosting Postgres. 
I picked Supabase for the managed Postgres instance, hosted dashboard, and built-in auth. This creates a tradeoff, as I have a free-tier limit, but the underlying database 
is still standard Postgres if I ever need to migrate.

