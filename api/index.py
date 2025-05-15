from flask import Flask, request, jsonify
import pandas as pd
import os
import re

app = Flask(__name__)

CSV_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")
allergen_df = pd.read_csv(CSV_PATH)


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


def map_ingredients_to_allergies(ingredients_list, allergen_df):
    mapped_data = {}
    for ingredient in ingredients_list:
        matches = allergen_df[
            allergen_df["ingredient"].str.lower() == ingredient.lower()
        ]
        if not matches.empty:
            mapped_data[ingredient] = matches.iloc[0]["allergy"]
    return mapped_data


@app.route("/preprocess", methods=["GET"])
def preprocess_api():
    ocr_text = request.args.get("ocr_text")

    if not ocr_text:
        return jsonify({"error": "Missing 'ocr_text' query parameter"}), 400

    try:
        ingredients_list = preprocess_text(ocr_text)
        mapped_data = map_ingredients_to_allergies(ingredients_list, allergen_df)
        result = {
            "ingredients": ingredients_list,
            "allegens": mapped_data,
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
