from groq import Groq

key = "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"

def analyze_code_with_llm(file_content, file_name):
    prompt = f""" 
        Analyze the following code for:
        - Code style and formatting issues
        - Potential bugs or errors
        - Performance improvements
        - Best practices

    File Name: {file_name}
    File Content: {file_content}

    Provide a detailed JSON output with the structure:
    {{
        "issues": [
            {{
                "issue": "<style>|bugs|performance>|best_practices",
                "line": <line_number>,
                "suggestion": <suggestion>
            }}
        ]
    }}
    ```json
    """

    client = Groq(
        api_key=key
    )
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        top_p=1
    )
    print(completion.choices[0].message.content)
    return completion