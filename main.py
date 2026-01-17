from model.naive_bayes import NaiveBayesClassifier

# clasify paragraph as safe or risky
def safety(paragraph):
    statements = []
    for line in paragraph.split("\n"):
        statement = line.strip()
        if not statement:
            continue
        statements.extend(statement.split("."))
        
    safe_risky = []
    risky_statements = []
    safe_count = 0
    risky_count = 0
    for statement in statements:
        result = nb.predict(statement)
        if result == "Safe":
            safe_count += 1
        else:
            risky_count += 1
            risky_statements.append(statement)
        safe_risky.append((statement, result))
    if risky_count > 0:
        overall = "Risky"
    else:
        overall = "Safe"
    total = safe_count + risky_count
    confidence = risky_count / total if total > 0 else 0.0
    return overall,confidence, risky_statements


# load dataset
Safe_statements = []
Risky_statements = []

with open("data/raw_statements.txt", "r") as f:
    for line in f:
        l_arr = line.strip().split("::")
        if len(l_arr) != 2:
            continue
        label, text = l_arr
        if label == "SAFE":
            Safe_statements.append(text)
        else:
            Risky_statements.append(text)

# train model
nb = NaiveBayesClassifier()
nb.train(Safe_statements, Risky_statements)

# terminal input
lines = []
while True:
    statement = input("Enter a statement (type END to finish): ").strip()
    if statement.lower() == "end":
       break
    lines.append(statement)
paragraph = "\n".join(lines)
result,confidence,risky_statements = safety(paragraph)
print(f"The overall classification of the paragraph is: {result}")
print(f"Confidence level: {confidence:.2f}")
if result == "Risky":
    print("Risky statements identified:")
    for i, stmt in enumerate(risky_statements, 1):
        print(f"{i}. {stmt}")

