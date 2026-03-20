import pandas as pd
import random
from datetime import datetime, timedelta

products = ["Phone X", "Laptop Pro", "Smartwatch Z", "Tablet S", "Earbuds Q"]

issues = [
    "battery drains fast",
    "screen not working",
    "delivery delayed",
    "payment failed",
    "device overheating",
    "app crashes",
    "no sound",
    "wifi disconnects",
    "camera blurred",
    "shipment lost"
]

cities = ["Kolkata", "Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow"]

categories = ["Hardware", "Software", "Delivery", "Billing", "Network"]

urgency = ["Low", "Medium", "High", "Critical"]

num_records = 10000

data = []

start_date = datetime(2025, 1, 1)

for i in range(num_records):
    product = random.choice(products)
    issue = random.choice(issues)
    city = random.choice(cities)
    category = random.choice(categories)
    priority = random.choices(urgency, weights=[35, 40, 20, 5], k=1)[0]
    complaint_date = start_date + timedelta(days=random.randint(0, 365))
    complaint = f"My {product} has an issue: {issue}."

    data.append({
        "id": i + 1,
        "product": product,
        "city": city,
        "category": category,
        "priority": priority,
        "complaint_date": complaint_date.strftime("%Y-%m-%d"),
        "complaint": complaint
    })

# Save as the main file and leave compatibility with original name

full_df = pd.DataFrame(data)
full_df.to_csv("complaints_10k.csv", index=False)
full_df.to_csv("complaints.csv", index=False)

print(f"Dataset created with {num_records} rows in complaints_10k.csv and complaints.csv")
