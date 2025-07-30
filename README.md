# SafeEats - Allergy Detection API

![Flask](https://img.shields.io/badge/flask-%e543405e.svg?style=for-the-badge&logo=flask&logoColor=white)
![APIs](https://img.shields.io/badge/apis-%3485354.svg?style=for-the-badge&logo=&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23644e.svg?style=for-the-badge&logo=vercel&logoColor=white)
![Python](https://img.shields.io/badge/python-%348e.svg?style=for-the-badge&logo=python&logoColor=white)

SafeEats is an intelligent allergy detection system that helps users identify potential allergens in food products by analyzing ingredient lists. This production-ready API serves as a Backend for Frontend (BFF) service, processing OCR text from food labels and mapping ingredients to known allergens.

## 🌟 Features

- **Ingredient Text Processing**: Cleans and extracts ingredients from OCR text
- **Allergen Mapping**: Maps ingredients to their corresponding allergens using a comprehensive dataset
- **Production Ready**: Deployed on Vercel with serverless functions
- **RESTful API**: Simple GET endpoint for easy integration

## 🚀 Production Deployment

The SafeEats API is deployed and available at: **https://allergydetectionsafeeats.app/preprocess**

### API Endpoint

```
GET /preprocess?ocr_text=<ingredient_text>
```

**Example Request:**

```bash
curl "https://allergydetectionsafeeats.app/preprocess?ocr_text=ingredients%20wheat%20flour%20Milk%20%2886%25%29%2C%20eggs%2C%20Cocoa%20Solids%20%281.4%25%29%2C%20soy%20%28lecithun%20415%2C%29%2C%20Sequestrant%20%28INS%20451%20%28i%29%29%2C%20lodized
"
```

**Example Response:**

```json
{
  "ingredients": ["wheat flour", "milk", "eggs", "soy lecithin"],
  "allergens": {
    "wheat flour": "gluten",
    "milk": "dairy",
    "eggs": "eggs",
    "soy lecithin": "soy"
  }
}
```

## 🛠️ How it Works

This application uses Flask 3 with Vercel's serverless functions to:

1. **Text Preprocessing**: Cleans OCR text and extracts ingredient lists
2. **Allergen Detection**: Maps each ingredient against a comprehensive allergen database
3. **Response Generation**: Returns structured JSON with ingredients and their associated allergens

The system is designed to handle real-world OCR text with various formatting inconsistencies and extract meaningful ingredient information.

## 🏃‍♂️ Running Locally

```bash
# Install Vercel CLI
npm i -g vercel

# Start development server
vercel dev
```

Your Flask application will be available at `http://localhost:3000`.

## 📁 Project Structure

```
├── api/
│   ├── index.py              # Main Flask application
│   ├── allergen_dataset.csv  # Allergen mapping database
│   └── dataset.csv           # Additional dataset
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel configuration
└── README.md                # This file
```

## 🧪 Capstone Project

This is part of a 7th semester capstone project focused on food safety and allergy detection technology. The BFF architecture enables seamless integration with frontend applications while providing robust allergen detection capabilities.
