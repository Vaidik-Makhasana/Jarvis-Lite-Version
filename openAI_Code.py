from openAI_Code import OpenAI
client = OpenAI(
    api_key="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"
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistent assistant named Gemini skilled in general tasks"},
        {
            "role": "user",
            "content": "What is coding"
        }
    ]
)

print(completion.choices[0].message)