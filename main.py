import pandas as pd
import openai
import csv
"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"
openai.api_key = "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"

request = "rate ten reviews from 1 to 10 and send in csv format:"
reviews = pd.read_excel("file.xlsx", sheet_name="Data")
full_rev = [str(i + 1) + ". " + reviews["review text"][i] + "\n" for i in range(10)]
emails = [reviews["email"][i] for i in range(10)]
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"{request} {''.join(full_rev)}",
    temperature=0.7,
    max_tokens=643,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
k = ((response.choices[0].text).split("\n"))
k = k[1].split(",")
with open('data.csv', 'w', newline="") as f:
    wr = csv.writer(f)
    wr.writerows([(k[i], emails[i]) for i in range(len(k))])
