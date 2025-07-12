from flask import Flask, request, jsonify
from flask_cors import CORS
import openai, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/enhance", methods=["POST"])
def enhance():
    data = request.get_json()
    prompt = data.get("text", "")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You polish resume skills and convert basic lines into professional descriptions."},
                {"role": "user", "content": f"Polish this: {prompt}"}
            ]
        )
        return jsonify({"output": response.choices[0].message["content"].strip()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
