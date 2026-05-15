# Mutant-IQ: AI-Powered Genetic Mutation Pathogenicity Predictor

Mutant-IQ is a machine learning platform designed to predict whether genetic mutations are **Pathogenic** or **Benign**. By leveraging Random Forest classification and advanced data balancing techniques like SMOTE, Mutant-IQ provides high-accuracy insights into the functional impact of genetic variants.

## 🧬 Overview

In the field of genomics, identifying the pathogenicity of a mutation is crucial for clinical diagnosis and research. Mutant-IQ automates this process by analyzing:
- **Gene**: The specific gene where the mutation occurs.
- **Mutation Type**: The nature of the genetic change (e.g., Missense, Nonsense, Frameshift).

## 🚀 Features

- **Machine Learning Core**: Powered by a Random Forest Classifier for robust and interpretable predictions.
- **Data Balancing**: Implements **SMOTE** (Synthetic Minority Over-sampling Technique) to handle class imbalances, ensuring the model performs well on rare pathogenic cases.
- **Automated Preprocessing**: Uses One-Hot Encoding to transform categorical genomic data into a machine-readable format.
- **Performance Metrics**: Comprehensive evaluation including Accuracy, Precision, Recall, and F1-Score.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Data Analysis**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Imbalance Handling**: Imbalanced-learn (SMOTE)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ananthapadmanabhan333/Mutant-IQ.git
   cd Mutant-IQ
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install pandas scikit-learn imbalanced-learn
   ```

## 🖥️ Usage

Ensure your dataset (`pathogenicity_data.csv`) is in the root directory. Run the predictor script:

```bash
python mutation_predictor.py
```

The script will:
1. Load and preprocess the data.
2. Apply SMOTE to balance the classes.
3. Train the Random Forest model.
4. Output evaluation metrics and a confusion matrix.

## 📊 Dataset Structure

The model expects a CSV file (`pathogenicity_data.csv`) with the following columns:
- `Gene`: Categorical name of the gene.
- `Mutation_Type`: Categorical type of mutation.
- `Pathogenicity`: Target label (**Pathogenic** or **Benign**).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Developed by [Ananthapadmanabhan](https://github.com/Ananthapadmanabhan333)
