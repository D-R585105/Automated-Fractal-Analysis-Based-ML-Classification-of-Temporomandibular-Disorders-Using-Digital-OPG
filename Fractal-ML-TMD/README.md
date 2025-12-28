# Fractal Analysis–Based Machine Learning Classification of Temporomandibular Disorders Using Digital OPGs

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7%2B-red)

## Overview

This repository contains the complete analysis pipeline used to perform **fractal dimension (FD)–based machine learning (ML) classification** of temporomandibular disorder (TMD) patients and healthy controls using digital orthopantomographs (OPGs).

The workflow integrates:

- Automated fractal analysis of mandibular condyles using ImageJ macros
- Feature extraction (right and left condylar FD)
- Machine learning classification using multiple algorithms
- Performance evaluation using cross-validated metrics

This repository is provided to ensure **transparency**, **reproducibility**, and **methodological clarity**.

---

## Study Design Summary

| Parameter | Description |
|-----------|-------------|
| **Sample Size** | 220 digital OPGs (110 TMD + 110 healthy controls) |
| **Matching** | Age- and gender-matched case-control design |
| **Age Groups** | 18–29, 30–39, 40–49, ≥50 years |
| **Imaging Modality** | Digital orthopantomographs (OPGs) |
| **Regions of Interest** | Right and left mandibular condyles |
| **Software** | ImageJ 1.42 (fractal analysis), Python (ML) |

---

## Repository Structure

```
Fractal_ML_TMD/
├── ML_Models.py              # Main ML classification pipeline
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── LICENSE                   # MIT License
│
├── sample_data/
│   └── fractal_features.csv  # Synthetic dataset (441 samples)
│
├── results/
│   └── ML_performance_metrics.csv  # Model performance output
│
└── ImageJ-Macros/            # Automated fractal analysis macros
    ├── Automated-Fractal-Analysis.ijm  # Main ImageJ macro script
    ├── Sample-Image/         # Sample OPG image for testing
    ├── Results/              # Output directory for processed images
    └── Previous Results/     # Example results (Left/Right Condyle FA)
```

---

## Important Note on Data

> **⚠️ DISCLAIMER:** The dataset included in the `sample_data/` directory is **synthetic** and does not contain real patient information.

- Synthetic data were generated to demonstrate code functionality and expected algorithmic behavior
- Actual patient data cannot be shared publicly due to ethical and institutional restrictions
- Performance results obtained using synthetic data **do not represent** the true clinical performance reported in the manuscript

---

## Feature Description

| Feature | Description | Data Type |
|---------|-------------|-----------|
| `FD_right` | Fractal dimension of right mandibular condyle | Float (1.18–1.47) |
| `FD_left` | Fractal dimension of left mandibular condyle | Float (1.19–1.47) |
| `age` | Patient age in years | Integer (18–64) |
| `gender` | Patient sex | Binary (0=Female, 1=Male) |
| `label` | Diagnostic classification | Binary (0=Healthy, 1=TMD) |

---

## Machine Learning Models

The following classifiers were evaluated with their respective hyperparameters:

| Model | Key Hyperparameters |
|-------|---------------------|
| **Logistic Regression** | C=1.0, solver='lbfgs', max_iter=1000 |
| **Support Vector Machine** | kernel='rbf', C=1.0, gamma='scale' |
| **K-Nearest Neighbors** | n_neighbors=5, weights='distance' |
| **Random Forest** | n_estimators=200, max_depth=None |
| **Gradient Boosting** | n_estimators=150, learning_rate=0.05, max_depth=3 |
| **XGBoost** | n_estimators=200, learning_rate=0.05, max_depth=4 |

All models use `random_state=42` for reproducibility.

---

## Model Evaluation

### Validation Strategy
- **Data Split:** 70% training / 15% validation / 15% test (stratified)
- **Random Seed:** 42 (fixed for reproducibility)

### Performance Metrics

| Metric | Description |
|--------|-------------|
| **Accuracy** | Overall classification correctness |
| **Precision** | Positive predictive value |
| **Recall** | Sensitivity / True positive rate |
| **F1-Score** | Harmonic mean of precision and recall |
| **ROC-AUC** | Area under receiver operating characteristic curve |

### Sample Results (Synthetic Data)

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.742 | 0.722 | 0.788 | 0.754 | 0.831 |
| Support Vector Machine | 0.803 | 0.813 | 0.788 | 0.800 | 0.820 |
| K-Nearest Neighbors | 0.742 | 0.735 | 0.758 | 0.746 | 0.836 |
| Random Forest | 0.788 | 0.788 | 0.788 | 0.788 | 0.878 |
| Gradient Boosting | 0.758 | 0.774 | 0.727 | 0.750 | 0.877 |
| XGBoost | 0.803 | 0.813 | 0.788 | 0.800 | 0.874 |

*Note: These results are from synthetic data and do not reflect actual clinical performance.*

---

## Installation & Usage

### Prerequisites

- Python 3.8 or higher
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Fractal_ML_TMD.git
cd Fractal_ML_TMD
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- numpy ≥1.23
- pandas ≥1.5
- scikit-learn ≥1.3.0
- xgboost ≥1.7.5
- matplotlib ≥3.7
- seaborn ≥0.12

### 4. Run the ML Pipeline

```bash
python ML_Models.py
```

### 5. View Results

Results will be saved to: `results/ML_performance_metrics.csv`

---

## ImageJ Fractal Analysis Protocol

Fractal analysis of the mandibular condyles was performed using the **box-counting method** in ImageJ.

### Automated Macro

An automated ImageJ macro (`ImageJ-Macros/Automated-Fractal-Analysis.ijm`) is provided to streamline the fractal analysis workflow. The macro performs:

1. ROI extraction from the OPG image
2. Gaussian blur background subtraction
3. Binary conversion and morphological operations (erode, dilate)
4. Skeletonization of trabecular bone structure
5. Fractal box counting analysis

For detailed usage instructions, see the [ImageJ-Macros README](ImageJ-Macros/README.md).

### Manual Steps:

1. **Import** digital OPG into ImageJ (version 1.42 or later)
2. **Define ROI** on the mandibular condyle using polygon selection tool
3. **Convert** image to 8-bit grayscale
4. **Apply** thresholding to segment trabecular bone
5. **Run** `Analyze > Tools > Fractal Box Count`
6. **Record** the fractal dimension (D) value
7. **Repeat** for both right and left condyles
8. **Export** FD values to CSV for ML analysis

---

## Reproducibility & Transparency

This repository adheres to best practices for computational reproducibility:

- ✅ All ML hyperparameters explicitly defined in code
- ✅ Random seeds fixed (`RANDOM_SEED = 42`)
- ✅ Synthetic data provided for pipeline validation
- ✅ Stratified splits to maintain class balance
- ✅ StandardScaler applied for distance-based models
- ✅ Complete requirements.txt for environment replication

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Citation

If you use or adapt this work, please cite the corresponding manuscript: 
Raut S N, Patil P B (December 27, 2025) Automated Fractal Analysis of Right and Left Condyles on Digital Panoramic Images Among Patients With Temporomandibular Disorder (TMD) and Use of Machine Learning Algorithms in the Diagnosis of TMD. Cureus 17(12): e100165. https://doi.org/10.7759/cureus.100165

```bibtex
@article{Raut S N, Patil P B (December 27, 2025),
  title={Automated Fractal Analysis of Right and Left Condyles on Digital Panoramic Images Among Patients With Temporomandibular Disorder (TMD) and Use of Machine Learning Algorithms in the Diagnosis of TMD.},
  author={[Raut S N, Patil P B]},
  journal={[Cureus Journal of Medical Science]},
  year={[2025]},
  doi={[10.7759/cureus.100165]}
}
}
```

---

## Contact

For questions regarding methodology or code:

- **Corresponding Author:** [Dr.Sumeet N. Raut]
- **Email:** [dr.sumeet.raut143@gmail.com]
- **Institution:** [Oral Medicine and Radiology, Employees' State Insurance Corporation Dental College and Hospital, Kalaburagi, INDIA]

---

## Disclaimer

This repository is intended **solely for academic and research purposes**. The synthetic data and demonstration results must not be interpreted as diagnostic or clinical evidence. This code is not intended for clinical decision-making.

---

*This repository was structured to meet biomedical imaging journal standards for code transparency and ethical data sharing.*
