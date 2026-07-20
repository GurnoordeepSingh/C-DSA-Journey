import os
cpp_files = sorted(
    [f for f in os.listdir() if f.endswith(".cpp")]
)
if not cpp_files:
    day_number = 0
else:
    last_file = cpp_files[-1]
    day_number = int(last_file[4:7])

next_day = day_number + 1
new_filename = f"day-{next_day:03}.cpp"


template = f"""/*
DAY: {next_day}

TOPIC:

LEETCODE:
- None

NOTES:

*/


"""
if os.path.exists(new_filename):
    print("❌ File already exists!")
else:
    # create the file
    with open(new_filename, "w", encoding="utf-8") as file:
        file.write(template)
    print(f"✅ Created {new_filename}")
