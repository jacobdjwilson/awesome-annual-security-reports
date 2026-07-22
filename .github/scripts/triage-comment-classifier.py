import os
import sys
import json
import argparse
import textwrap
import re

try:
    from google import genai
    from google.genai import types
    USE_NEW_SDK = True
except ImportError:
    try:
        import google.generativeai as genai
        USE_NEW_SDK = False
    except ImportError:
        print("ERROR: google-generativeai package required", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--comment", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("valid=false")
        return 0

    prompt = textwrap.dedent(f"""
    You are evaluating a human reviewer's comment on an automated security report discovery issue.
    
    Issue Title: {args.title}
    Human Comment: "{args.comment}"
    
    Classify the intent of the human's comment into one of the following exact JSON outputs. Respond ONLY with the JSON block. No markdown fencing, no explanation.

    If the human intends to ACCEPT the report as a valid discovery (e.g., "true positive", "looks good", "approve", "accept"):
    {{
      "outcome": "true_positive",
      "valid": "true",
      "label": "accepted",
      "close": "false"
    }}

    If the human intends to REJECT it because it's a DUPLICATE (e.g., "duplicate", "already exists", "already in repo"):
    {{
      "outcome": "duplicate",
      "valid": "true",
      "label": "duplicate",
      "close": "true"
    }}

    If the human intends to REJECT it as a FALSE POSITIVE (e.g., "false positive", "not a report", "financial report", "wrong topic", "bad domain"):
    {{
      "outcome": "false_positive",
      "valid": "true",
      "label": "false-positive",
      "close": "true"
    }}
    
    If the human intends to REJECT it as a MISMATCH (e.g., "wrong year", "old report", "wrong edition", "mismatch"):
    {{
      "outcome": "mismatch",
      "valid": "true",
      "label": "mismatch",
      "close": "true"
    }}
    
    If the human is just chatting, asking for help, or the intent is unclear:
    {{
      "valid": "false"
    }}
    """).strip()

    try:
        if USE_NEW_SDK:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    max_output_tokens=100
                ),
            )
            raw = response.text.strip()
        else:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(prompt)
            raw = response.text.strip()
            
        raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
        raw = re.sub(r"\s*```$", "", raw, flags=re.MULTILINE)
        result = json.loads(raw)
        
        # Fallback for GITHUB_OUTPUT format
        for k, v in result.items():
            print(f"{k}={v}")
            
    except Exception as e:
        print("valid=false")
        print(f"error={str(e)}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
