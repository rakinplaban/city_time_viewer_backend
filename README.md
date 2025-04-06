# 🌃 City Time Viewer Backend 🌃

**Hey there. I’m Madison.** 🕰️ Sitting on the rooftop with the glowing city behind me, I’ll guide you through this project with a calm smile and sharp mind. Let’s take a moment to admire the world—one time zone at a time.

<!-- <img src="static/202532222373833.png" height=300 width=200> -->
![Madison](static/202532222373833.png)

## 🌍 What is this?

This is a **Flask API** that helps you find the **current time** in any city you ask for. You tell me the city, and I’ll quietly fetch the accurate **timezone and time** for you. Clear, precise, and efficient—just how I like it.

## 🛠️ How does it work?

1. You provide a **city name** like "Tokyo" or "Paris". 🏙️  
2. I check the **coordinates** using Geonames. 🗺️  
3. I determine the **timezone** and fetch the **current time** for you using timezonedb API. 🕒  
4. I return a well-formatted JSON response with everything you need. 📦  

## 🧭 How to use it?

1. Set up your virtual environment:
   ```sh
   python -m venv .venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the necessary dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the backend:
   ```sh
   flask run
   ```

## 🕰️ Requesting the time

Send a GET request like this:
```
GET /api/time?city=London
```
And I’ll respond with something like:
```json
{
    "abbreviation": "BST",
    "city": "London",
    "current_time": "2025-03-30 16:14:03",
    "formatted": "16:14:03 (BST)",
    "timezone": "Europe/London",
    "timezone_offset": 3600
}
```

## 📌 Notes

- Too many requests in a short time? You might be rate-limited. Let’s not rush—time moves steadily for everyone. ⏳  

## 💛 Support

If this project helped you, **Star 🌟 This Repo** and let Madison keep watching over your city clocks from her rooftop.  
The world’s time is in good hands.

---

That’s all for now. Whether it’s midnight in Tokyo or dawn in New York, Madison’s got you covered. Stay sharp. 🖤🌃🕰️

