import base64

code_str = 'ZnJvbSBkamFuZ28udGVzdCBpbXBvcnQgVGVzdENhc2UKCiMgQ3JlYXRlIHlv\ndXIgdGVzdHMgaGVyZS4K\n'

# print(base64.b64decode(code_str).decode())

# from urllib.parse import urlparse


# def get_owner_and_repo(url):
#     parsed_url = urlparse(url)
#     path_parts = parsed_url.path.strip('/').split('/')
#     print(path_parts)
#     if len(path_parts)>=2:
#         owner, repo = path_parts[0], path_parts[1]
#         return owner, repo
#     return None, None


# print(get_owner_and_repo("https://github.com/nagapure/Djnago_Email_OTP_Verification/pulls"))




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
    # return completion


analyze_code_with_llm((base64.b64decode(code_str).decode()), "tests.py")