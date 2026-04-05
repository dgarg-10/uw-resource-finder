const API_URL = import.meta.env.PROD
    ? "https://uw-campus-finder-backend.onrender.com/api"
    : "http://localhost:5001/api";


export function getUserId(){
    let userId = localStorage.getItem("campus_user_id")
    if(!userId){
        userId = "user_" + Math.random().toString(36).substring(2, 15)
        localStorage.setItem("campus_user_id", userId)
    }
    return userId
}

export async function getAllResources(){
    const response = await fetch(`${API_URL}/resources`)
    if(!response.ok){ //checks if 2XX status code was not passed
        throw new Error("Failed to fetch reources")
    }
    return response.json()
}

export async function getResourceHours(resourceId){
    const response = await fetch(`${API_URL}/resources/${resourceId}/hours`);
    if(!response.ok){
        throw new Error("Failed to fetch hours")
    }
    return response.json()
}

export async function getTodayHours(){
    const response = await fetch(`${API_URL}/hours/today`)
    if(!response.ok){
        throw new Error("Failed to fetch today's hours")
    }
    return response.json()
}

export async function getOpenNow(){
    const response = await fetch(`${API_URL}/resources/open`)
    if(!response.ok){
        throw new Error("Failed to fetch open resources")
    }
    return response.json()
}

export async function searchResources(query) {
    const response = await fetch(
      `${API_URL}/resources/search?q=${encodeURIComponent(query)}`
    );
    if (!response.ok) {
      throw new Error("Failed to search resources");
    }
    return response.json();
  }

export async function getFavorites(userID){
    const response = await fetch(`${API_URL}/favorites/${userID}`)
    if(!response.ok){
        throw new Error("Failed to fetch favorites list")
    }
    return response.json()
}

export async function addFavorite(userId, resourceId) {
    const response = await fetch(`${API_URL}/favorites`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, resource_id: resourceId }),
    });
    if (!response.ok) {
      throw new Error("Failed to add favorite");
    }
    return response.json();
}

export async function removeFavorite(userId, resourceId) {
    const response = await fetch(`${API_URL}/favorites`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, resource_id: resourceId }),
    });
    if (!response.ok) {
      throw new Error("Failed to remove favorite");
    }
    return response.json();
  }