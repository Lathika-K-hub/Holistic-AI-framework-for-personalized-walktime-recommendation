def chatbot_advice(stress, temp, humidity, duration, question=None):

    
    if question:
        question = question.lower()

        if any(word in question for word in ["hi", "hello", "hey", "hii"]):
            return "Hlo! How can I guide you?"

        
        if "diet" in question or "food" in question:
            return "🥗 Eat balanced food: vegetables, fruits, protein and drink plenty of water."

        
        elif "walk" in question and "time" in question:
            return f"🚶 Recommended walking time is {int(duration)} minutes daily."

        
        elif any(word in question for word in ["morning", "evening", "walk time"]):
            if temp > 32:
                return "🌅 Weather is hot — morning or evening walk is best."
            elif temp < 20:
                return "🌞 Morning walk is better in cold weather."
            else:
                return "✅ Both morning and evening are good for walking."

        
        elif "stress" in question:
            return f"🧠 Your stress level is {stress}. Try meditation, breathing exercises, or light walking."

        
        elif "weather" in question or "temperature" in question:
            return f"🌤 Temperature: {temp}°C, Humidity: {humidity}%."

    
        elif "sleep" in question:
            return "😴 Sleep at least 7–8 hours daily for good health."

        
        elif "water" in question or "hydration" in question:
            return "💧 Drink 2–3 litres of water daily (more in hot weather)."

        
        elif "exercise" in question:
            return "🏃 Regular walking, stretching, or yoga keeps you healthy."

        else:
            return "🙂 Ask me about diet, walking, stress, sleep, weather, or exercise."

    
    if temp > 35:
        weather_msg = "⚠ Weather is hot. Prefer morning or evening walk."
    elif temp < 20:
        weather_msg = "❄ Cold weather. Wear warm clothes."
    else:
        weather_msg = "✅ Weather looks good for walking."

    humidity_msg = "💧 High humidity detected. Stay hydrated." if humidity > 80 else ""

    if stress == "High":
        stress_msg = "😌 Try slow walking, meditation, and breathing exercises."
    elif stress == "Medium":
        stress_msg = "🚶 Moderate walking recommended."
    else:
        stress_msg = "👍 Good stress level. Maintain your routine."

    return f"""
🤖 Health Recommendation

🚶 Recommended Walking Time: {int(duration)} minutes

{weather_msg}
{humidity_msg}
{stress_msg}

Stay healthy 😊
"""
