from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# checking
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

@app.route('/preprocess', methods=['GET'])
def preprocess_api():
    ocr_text = request.args.get('ocr_text')
    if not ocr_text:
        return jsonify({"error": "Missing 'ocr_text' query parameter"}), 400

    try:
        result = preprocess_text(ocr_text)
        return jsonify({"ingredients": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
