# Past exam papers (each inner list shows topics asked in order)
past_papers = [
    ["Loops", "Functions", "Lists", "Strings"],
    ["Loops", "Lists", "Dictionaries", "Files"],
    ["Functions", "Lists", "Strings", "Dictionaries"],
    ["Loops", "Functions", "Dictionaries", "Files"],
    ["Lists", "Strings", "Files", "Functions"]
]

print("--- EXAM QUESTION PREDICTOR (AIML) ---")
print("Available Topics: Loops, Functions, Lists, Strings, Dictionaries")
current_topic = input("Enter current question topic: ").strip().title()

# Step 1: Count which topic comes next using a basic dictionary
next_topic_counts = {}
total_matches = 0

for paper in past_papers:
    for i in range(len(paper) - 1):
        if paper[i] == current_topic:
            next_topic = paper[i + 1]
            total_matches = total_matches + 1

            if next_topic in next_topic_counts:
                next_topic_counts[next_topic] = next_topic_counts[next_topic] + 1
            else:
                next_topic_counts[next_topic] = 1

# Step 2: Calculate percentage and find the highest probability topic
if total_matches == 0:
    print("Topic not found in past papers.")
else:
    print("\nPrediction Results:")
    best_topic = ""
    highest_count = 0

    for topic in next_topic_counts:
        count = next_topic_counts[topic]
        probability = (count / total_matches) * 100
        print(f"- {topic}: {probability:.0f}% chance")

        if count > highest_count:
            highest_count = count
            best_topic = topic

    print(f"\nMost Likely Next Question: {best_topic}")
