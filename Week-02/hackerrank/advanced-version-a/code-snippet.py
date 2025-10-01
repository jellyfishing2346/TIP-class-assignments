gradebook = {
    "class": {
        "student": {
            "name": "Mike",
            "grade": {
                "physics": 'C',
                "history": 'B'
            }
        }
    }
}

print(gradebook['class']['student']['grade']['history'])