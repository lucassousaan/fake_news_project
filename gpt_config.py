import csv
import openai
import time
from config import api_key

openai.api_key = api_key
model = "text-davinci-002"

def generate_classification(prompt):
    while True:
        try:
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                temperature=0.2,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return (response.choices[0].text.strip())
        except openai.error.RateLimitError as e:
            print(f"Rate limit reached. Waiting for 60 seconds...")
            time.sleep(60)
            continue
        except openai.error.APIError as e:
            # If all the free trial tokens are used, save the results and exit
            if e.status == 402 or e.status == 403:
                print(f"Maximum usage limit reached. Saving results and exiting...")
                break
            else:
                raise e

csvFinalResult = open('results/classification_result.csv', 'w', newline='')
writerResult = csv.writer(csvFinalResult) 
data = []
with open("results/dataset_label_shuffled.csv", 'rt') as fileFake:
    reader = csv.reader(fileFake)
    next(reader)
    for row in reader:
        prompt = "'" + row[1] + "' Does the given text is a fake news? It Spreads misinformation? Answer only with yes or no."
        classification = generate_classification(prompt)
        data.append([row[1], row[3], classification])
    writerResult.writerow(['text', 'is_fake_news', 'gpt_classification'])
    writerResult.writerows(data)
    fileFake.close()
