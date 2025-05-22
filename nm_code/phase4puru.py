import pandas as pd
import numpy as np
import time

# Sample user data (can also be read from a CSV)
user_data = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "email": ["alice@example.com", "bob@example.com", "charlie@example.com"],
    "interests": ["fitness, nutrition", "technology, AI", "travel, nature"]
})

# Email templates dictionary
email_templates = {
    "fitness": {
        "subject": "Top Fitness Tips Just for You",
        "content": "Discover easy workouts and healthy habits to stay in shape!"
    },
    "nutrition": {
        "subject": "Eat Smart: Nutrition Advice",
        "content": "Check out our latest tips on healthy eating and balanced diets."
    },
    "technology": {
        "subject": "Explore the Latest Tech Trends",
        "content": "Stay updated with breakthroughs in AI and technology."
    },
    "AI": {
        "subject": "The Future is AI",
        "content": "Learn how AI is shaping industries and what’s next."
    },
    "travel": {
        "subject": "Travel Destinations You’ll Love",
        "content": "Plan your next adventure with our top travel picks!"
    },
    "nature": {
        "subject": "Reconnect with Nature",
        "content": "Explore beautiful places and nature activities around the world."
    }
}

# Match user interest to best email template (first match approach)
def get_best_template(user_interests):
    interests_list = [i.strip().lower() for i in user_interests.split(',')]
    
    for interest in interests_list:
        if interest in [key.lower() for key in email_templates.keys()]:
            for key in email_templates:
                if interest == key.lower():
                    return email_templates[key]
    
    # Default fallback
    return {
        "subject": "Stay Connected",
        "content": "We’ll keep you updated with news you’ll love."
    }

# Simulate sending emails
def send_email(name, email, template):
    print(f"\nTo: {email}")
    print(f"Subject: {template['subject']}")
    print(f"Hi {name},\n{template['content']}\n")

# Track performance
start_time = time.time()
print("Starting personalized email campaign...\n")

# Loop through users
for index, row in user_data.iterrows():
    template = get_best_template(row["interests"])
    send_email(row["name"], row["email"], template)

end_time = time.time()
print(f"\nCampaign completed in")
