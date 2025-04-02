# ✨ City Time Viewer Backend ✨

**Hello there! I'm Hikari!** ☀️ ☀️ Standing here on the seashore with the warm sun shining down, I’d love to introduce you to this project with a bright smile! 🌊👒

<img src="static/202532222373833.png" height=300 width=200>

## 🌏 What is this?

This is a **Flask API** that helps you find the **current time** in any city you ask for! Just tell me the city, and I’ll fetch the correct **timezone and time** for you. Simple and sunny, right? ☀️🕰️

## 🛠️ How does it work?

1. You provide a **city name** like "Tokyo" or "Paris"! 🏙️
2. I check the **coordinates** using Geonames. 🗺️
3. I determine the **timezone** and fetch the **current time** for you using timezonedb API! 🕒
4. I return a friendly JSON response with all the details! 😊

## 🎮 How to use it?

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

## ☀️ Requesting the time!

Send a GET request like this:
```
GET /api/time?city=London
```
And I will happily respond with:
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

## 🌊 Notes
<!-- - You **must** set a **User-Agent** in your requests, or OpenStreetMap might not allow access. -->
- Too many requests in a short time could lead to temporary blocking—so take it easy! 😌

## 💛 Support
If you like this project, **Star 🌟 This Repo** and keep smiling under the sunny skies! ☀️

---

That’s all for now! Enjoy using this API and have a wonderful day! 😊🌊👒

