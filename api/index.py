from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def preprocess_text(ocr_text):
    def clean_text(text):
        text = text.lower()
        text = re.sub(r"^.*?ingredients:", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"ingredients:", "", text, flags=re.IGNORECASE)
        text = re.sub(r"[^a-zA-Z, ]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def split_ingredients(text):
        ingredients = text.split(",")
        ingredients = [ing.strip() for ing in ingredients if ing.strip()]
        return ingredients

    cleaned_text = clean_text(ocr_text)
    ingredients_list = split_ingredients(cleaned_text)
    return ingredients_list

@app.route('/preprocess', methods=['POST'])
def preprocess_api():
    data = request.get_json()
    if not data or 'ocr_text' not in data:
        return jsonify({"error": "Missing 'ocr_text' in request"}), 400
    
    ocr_text = data['ocr_text']
    try:
        result = preprocess_text(ocr_text)
        return jsonify({"ingredients": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
