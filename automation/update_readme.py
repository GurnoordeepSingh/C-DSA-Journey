import os

cpp_files = sorted([f for f in os.listdir() if f.endswith(".cpp")])

all_days = []

for file in cpp_files:

    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    day_data = {
        "day": "",
        "topic": [],
        "leetcode": [],
        "notes": []
    }

    section = None

    for line in lines:

        line = line.strip()

        if line.startswith("DAY:"):
            day_data["day"] = line.replace("DAY:", "").strip()

        elif line == "TOPIC:":
            section = "topic"

        elif line == "LEETCODE:":
            section = "leetcode"

        elif line == "NOTES:":
            section = "notes"

        elif line.startswith("*/"):
            section = None

        elif line and section:

            if section == "topic":
                day_data["topic"].append(line)

            elif section == "leetcode":
                day_data["leetcode"].append(line.replace("- ", ""))

            elif section == "notes":
                day_data["notes"].append(line)

    all_days.append(day_data)


# ===============================
# Generate README
# ===============================

with open("README.md", "w", encoding="utf-8") as readme:

    readme.write("# 🚀 C++ DSA Journey\n\n")
    

    
    total_questions = sum(len(day["leetcode"]) for day in all_days)
    topics = set()

    for day in all_days:
        for topic in day["topic"]:
            topics.add(topic)

    total_topics = len(topics)

    latest_day = all_days[-1]["day"] if all_days else "0"
    
    goal = 100

    completed = len(all_days)

    percentage = int((completed / goal) * 100)

    filled_blocks = percentage // 5

    progress_bar = "█" * filled_blocks + "░" * (20 - filled_blocks)
    # NOW write the README
    readme.write("# 🚀 C++ DSA Journey\n\n")

    readme.write("![Language](https://img.shields.io/badge/Language-C%2B%2B-blue?style=flat-square)\n")
    readme.write(f"![Days](https://img.shields.io/badge/Days-{completed}-brightgreen?style=flat-square)\n")
    readme.write(f"![Problems](https://img.shields.io/badge/Problems-{total_questions}-orange?style=flat-square)\n")
    readme.write(f"![Topics](https://img.shields.io/badge/Topics-{total_topics}-purple?style=flat-square)\n\n")
    readme.write("> This README is automatically generated.\n\n")

    

    readme.write("## 📊 Dashboard\n\n")
    readme.write(f"{progress_bar} {percentage}%\n\n")

    readme.write(f"🎯 Goal : {goal} Days\n\n")

    readme.write(f"📅 Days Completed : **{len(all_days)}**\n\n")

    readme.write(f"🧩 Problems Solved : **{total_questions}**\n\n")

    readme.write(f"📚 Topics Learned : **{total_topics}**\n\n")

    readme.write(f"🔥 Latest Day : **{latest_day}**\n\n")

    readme.write("---\n\n")

    readme.write("## 📑 Table of Contents\n\n")

    for day in all_days:

        topic = day["topic"][0] if day["topic"] else "No Topic"

        readme.write(f"- [Day {day['day']} - {topic}](#day-{day['day']})\n")

    readme.write("\n---\n\n")

    for day in all_days:

        readme.write(f"## Day {day['day']}\n\n")

        readme.write("### 📚 Topics\n")

        for topic in day["topic"]:
            readme.write(f"- {topic}\n")

        readme.write("\n### 💻 LeetCode\n")

        for problem in day["leetcode"]:
            readme.write(f"- {problem}\n")

        readme.write("\n### 📝 Notes\n")

        for note in day["notes"]:
            readme.write(f"- {note}\n")

        readme.write("\n---\n\n")

print("✅ README generated successfully!")