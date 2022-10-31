import wolframalpha as w
question = input("Question: ")
app_id = "WJJGKH-WTJ3P5E3QP"
client = w.Client(app_id)
res = w.Client.query(question)
answer = next(res.results).text
print(answer)