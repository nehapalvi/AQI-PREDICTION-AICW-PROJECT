# utils/mapping.py

city_mapping = {
    0: "Ahmedabad",
    1: "Aizawl",
    2: "Amaravati",
    3: "Amritsar",
    4: "Bengaluru",
    5: "Bhopal",
    6: "Brajrajnagar",
    7: "Chandigarh",
    8: "Chennai",
    9: "Coimbatore",
    10: "Delhi",
    11: "Ernakulam",
    12: "Gurugram",
    13: "Guwahati",
    14: "Hyderabad",
    15: "Jaipur",
    16: "Jorapokhar",
    17: "Kochi",
    18: "Kolkata",
    19: "Lucknow",
    20: "Mumbai",
    21: "Patna",
    22: "Shillong",
    23: "Talcher",
    24: "Thiruvananthapuram",
    25: "Visakhapatnam"
}

# reverse mapping (VERY IMPORTANT)
reverse_city_mapping = {v: k for k, v in city_mapping.items()}