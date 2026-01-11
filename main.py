from graph import app

question = input("Ask your question: ")
user_id = input("Enter user id: ")

response = app.invoke({
    "question": question,
    "user_id": user_id
})

print("\n✅ Final Answer:\n")
print(response["answer"])
