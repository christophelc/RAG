from Rag import Rag

rag=Rag()
messages = [
        {
            "role" : "system",
            "content" : """
            You are an assistant who answers questions in a consise style. Provide answers according to the following sentences starting with kw:')
            """,
        },
]

#q = "How many flowers do you know ?"
q = "Could you list me the flowers you know ?"
result = rag.query(user_query = q, history = messages)
print(result)
