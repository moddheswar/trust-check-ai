from model.naive_bayes import NaiveBayesClassifier

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
while True:
    statement = input("Enter a statement (or 'exit' to quit): ").strip()
    if statement.lower() == "exit":
        break
    result = nb.predict(statement)
    print(f"Prediction: {result}")
