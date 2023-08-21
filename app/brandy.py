import os
import openai
import argparse

MAX_INPUT_LENGTH = 12


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if validate_length(user_input):
        branding_result = generate_branding_snippet(user_input)
        keywords_result = generate_keywords(user_input)
        print("branding text ", branding_result)
        print("keywords ", keywords_result)
    else:
        raise ValueError(
            f"Invalid input, must be less than {MAX_INPUT_LENGTH} chars! Submitted input is {user_input}"
        )
    pass


def validate_length(prompt: str):
    if len(prompt) < MAX_INPUT_LENGTH:
        return True


def generate_keywords(prompt: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate related keywords {prompt}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": enriched_prompt}],
        temperature=0.8,
        max_tokens=32,
    )
    keywords = response["choices"][0]["message"]["content"]
    return keywords


def generate_branding_snippet(prompt: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    subject = "coffee"
    enriched_prompt = f"Generate an upbeat branding snippet for {prompt}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": enriched_prompt}],
        temperature=0.8,
        max_tokens=32,
    )
    branding_text = response["choices"][0]["message"]["content"]

    branding_text = branding_text.strip()
    last_char = branding_text[-1]

    if last_char not in {"!", "?", "."}:
        branding_text = branding_text + "..."

    return branding_text


if __name__ == "__main__":
    main()
