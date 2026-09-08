# WHO WANTS TO BE MILLIONAIRE?

questions = [
    ["A", "Who is PM of India", "N modi", "Shahrukh khan", "Apurva", "Samay Raina"],
    ["A", "In which state Banaras is located?", "Uttar Pradesh", "Maharashtra", "Kerala", "Tamil Nadu"],
    ["B", "Capital of kerala", "Kochi", "Thiruvananthapuram", "Kannur", "Palakkad"],
    ["B", "1 million is how many lakhs?", "1", "10", "100", "1000"],
]

for q in questions:
    print(q[1])
    print("A.", q[2])
    print("B.", q[3])
    print("C.", q[4])
    print("D.", q[5])
    answer = input("Enter your answer: ")
    if answer.lower() == q[0].lower():
        print("Correct!")
    else:
        print("Incorrect! The correct answer is:", q[0])
        break
