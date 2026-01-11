# MY AI/ML LEARNING JOURNEY

<div align="center">
  <img src="https://img.shields.io/github/last-commit/pandeysulav/NEURONEXUS" alt="Last Updated" />
  <img src="https://img.shields.io/github/repo-size/pandeysulav/NEURONEXUS" alt="Repo Size" />
</div>

<br>

<div align="center">
    <img src="ASSETS/cover.png" alt="365 Days of AI/ML Learning cover" width="400" />
</div>

<div align="center">
    <a href="#bottom" title="Jump to today's entry">
        <img src="https://img.shields.io/badge/▼_Click_to_Navigate_to_Today-0D1117?style=for-the-badge&logoColor=white&labelColor=161B22" alt="Jump to Today" />
    </a>
</div>

> [!note]
> I'll share progress and demos on **LinkedIn** and **Twitter**.  
> Updates will be concise and focused on what I actually built or explored.

---

## Projects Completed

| Projects                                                                           | Description                                | Deployment                       |
| ---------------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------- |
| [Project Name](https://github.com/pandeysulav/NEURONEXUS/tree/main/project-folder) | Brief description of what the project does | [Live Demo](https://example.com) |
| [Project Name](https://github.com/pandeysulav/NEURONEXUS/tree/main/project-folder) | Brief description here                     | [Live Demo](https://example.com) |

---

## Resources

| Books & Courses                           | Completion Status |
| ----------------------------------------- | ----------------- |
| Essence of Linear Algebra @3Blue1Brown    | ✅                 |
| Machine Learning Specialization @Coursera | ✅                 |
| ML Playlist @CampusX                      | ⏳                 |
| Hands-On Machine Learning (Sklearn & TF)  | ⏳                 |
| MIT Intro to Deep Learning                | ⏳                 |
| Deep Learning Playlist @CampusX           | ⏳                 |
| Neural Networks @3Blue1Brown              | ⏳                 |
| fastai Deep Learning                      | ⏳                 |
| Karpathy Zero to Hero                     | ⏳                 |
| LangChain Intro @Pinecone                 | ⏳                 |
| ML Resources Web                          | ⏳                 |
| GenAI Handbook                            | ⏳                 |
| HF Deep RL Course                         | ⏳                 |
| RLHF Book                                 | ⏳                 |

---

## Daily Learning

---

### **Day 1: Introduction to Machine Learning**

**Date:** 2025-12-08  
**Day:** Day 1  
**Topic:** What is Machine Learning?

**What I Learned Today:**  

- Machine Learning is a subset of AI that enables computers to learn patterns from data.
- ML systems improve automatically through experience.
- Types of ML: Supervised, Unsupervised, Reinforcement Learning.
- Applications: recommendation systems, fraud detection, image recognition, NLP, etc.

**Key Insights:**  
Machine Learning is the foundation of modern AI systems. It enables data-driven predictions and decisions, forming the backbone of automation and intelligent applications.

![](./ASSETS/ml1.png)
![](./ASSETS/ml2.png)
![](./ASSETS/ml3.png)
![](./ASSETS/ml4.png)
![](./ASSETS/ml5.png)
![](./ASSETS/ml6.png)
![](./ASSETS/ml7.png)

---

### **Day 2: Major Uses & Functions of NumPy and Pandas**

**Date:** 2025-12-09  
**Day:** Day 2  
**Topic:** NumPy & Pandas Essentials

### **NumPy Overview**

- Foundation of numerical computing in Python.
- Supports multidimensional arrays.
- Fast mathematical operations using vectorization.
- Tools for random numbers, linear algebra, broadcasting, reshaping.

### **Key NumPy Functions Learned:**

- `np.array()`  
- `np.arange()`, `np.linspace()`  
- `reshape()`  
- Indexing & slicing  
- `np.mean()`, `np.sum()`, `np.max()`  
- `copy()` vs **views**

### **Pandas Overview**

- Best library for working with structured/tabular data.
- Provides **Series** (1D) and **DataFrames** (2D).
- Ideal for cleaning, wrangling, preprocessing.

### **Key Pandas Functions Learned:**

- `pd.Series()`, `pd.DataFrame()`  
- `read_csv()`  
- `.head()`, `.info()`, `.describe()`  
- `.loc[]` and `.iloc[]`  
- Handling missing values: `.isnull()`, `.fillna()`  
- Filtering, grouping, merging

**Key Insights:**  
NumPy accelerates mathematical operations, while Pandas simplifies working with structured datasets — together forming the backbone of ML workflows.

![](./ASSETS/ml8.png)
![](./ASSETS/ml9.png)
![](./ASSETS/ml10.png)
![](./ASSETS/ml11.png)
![](./ASSETS/ml12.png)

---

### **Day 3: Seaborn, Matplotlib & Essential Pandas Visualization**

**Date:** 2025-12-10  
**Day:** Day 3  
**Topic:** Intro to Visualization (Matplotlib, Seaborn, Pandas)

**Resources Used Today:**  
- **CampusX Visualization Playlist:** https://youtu.be/3Xc3CA655Y4  
- **Krish Naik Visualization Tutorial:** https://youtu.be/0P7QnIQDBJY  

### **Matplotlib Basics**
- Foundation plotting library in Python.
- Learned:
  - `plt.plot()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.show()`
- Understood axes, figures, subplots.

### **Seaborn Overview**
- Built on top of Matplotlib.
- Provides beautiful and statistical plots.
- Learned:
  - `sns.countplot()`  
  - `sns.barplot()`  
  - `sns.histplot()`  
  - `sns.pairplot()`  
- Themes:
  - `sns.set_style("whitegrid")`

### **More Pandas Visualization**
- Pandas integrates directly with Matplotlib.
- Used `.plot()` for:
  - Line charts  
  - Bar charts  
  - Histograms
- Learned sorting & grouping for better visualization preparation.

**Key Insights:**  
Visualization helps understand distributions, relationships, and patterns — a crucial step before applying ML algorithms.

![](./ASSETS/ml13.png)
![](./ASSETS/ml14.png)
![](./ASSETS/ml15.png)
![](./ASSETS/ml16.png)

---

### **Day 4: Exploratory Data Analysis (EDA)**

**Date:** 2025-12-12  
**Day:** Day 4  
**Topic:** EDA using Pandas, Seaborn & Matplotlib

**What I Learned Today:**  

- **EDA Overview:** Understanding dataset structure, detecting missing values, identifying outliers, visualizing distributions and correlations.
- Checked **missing data** using `train.isnull()` and `sns.heatmap()`.
- Dropped unnecessary columns like `Cabin`.
- Imputed missing `Age` values based on passenger class.
- One-hot encoded categorical variables (`Embarked`) using `pd.get_dummies()`.
- Visualized distributions with `sns.histplot`, `sns.displot`.  
- Countplots for categorical data like `SibSp`, `Pclass`, `Embarked`.

**Key Insights:**  
EDA helps uncover patterns, detect anomalies, and prepare data for ML modeling — it is a critical first step in any ML project.

![](./ASSETS/ml17.png)
![](./ASSETS/ml18.png)
![](./ASSETS/ml19.png)
![](./ASSETS/ml20.png)

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)

---

### **Day 5: Introduction to Object-Oriented Programming (OOP) in Python**

**Date:** 2025-12-13  
**Day:** Day 5  
**Topic:** OOP Concepts in Python

**What I Learned Today:**  

- **OOP Overview:** Programming paradigm based on objects and classes.
- Key concepts in Python:
  - **Class:** Blueprint for creating objects.
  - **Object/Instance:** Real entity created from a class.
  - **Attributes:** Variables that belong to an object (properties).
  - **Methods:** Functions that belong to a class (behaviors).
  - **Encapsulation:** Keeping data safe inside objects using public/private variables.
  - **Inheritance:** Reusing code from parent class in child class.
  - **Polymorphism:** Same interface, different implementation.
  - **Abstraction:** Hiding complex implementation details from the user.

**Key Insights:**  
OOP allows building modular, reusable, and maintainable code — essential for structuring ML projects and creating custom classes for models, datasets, and pipelines.

![](./ASSETS/ml21.png)
![](./ASSETS/ml22.png)
![](./ASSETS/ml23.png)
![](./ASSETS/ml24.png)
![](./ASSETS/ml25.png)
![](./ASSETS/ml26.png)
![](./ASSETS/ml27.png)

**Resources Used Today:**  
- [Krish Naik Machine Learning Playlist](https://youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe&si=J4ArLgWFJbz8tsWA)

---

### **Day 6: Working with CSV, JSON, SQL & APIs**

**Date:** 2025-12-14  
**Day:** Day 6  
**Topic:** Data Manipulation

**What I Learned Today:**  

- **CSV:** Loaded structured datasets using `pd.read_csv()` and explored tabular data efficiently.
- **JSON:** Worked with nested and structured JSON data using `pd.read_json()` and API responses.
- **SQL:** Understood how Python connects with databases to fetch data using SQL queries.
- **APIs:** Learned how to fetch real-time data from public APIs and convert responses into DataFrames.

**Key Insights:**  
Most real-world ML pipelines rely on external data sources like files, databases, and APIs. Mastering these formats is essential for practical data-driven applications.

![](./ASSETS/ml28.png)
![](./ASSETS/ml29.png)
![](./ASSETS/ml30.png)
![](./ASSETS/ml31.png)
![](./ASSETS/ml32.png)

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)

---

### **Day 7: Web Scraping, API Data Extraction & Understanding Your Data**

**Date:** 2025-12-15  
**Day:** Day 7  
**Topic:** Data Collection & Analysis

**What I Learned Today:**

#### **Web Scraping Fundamentals**

- **Beautiful Soup:** Parse HTML/XML content from websites using `bs4`.
- **Requests Library:** Fetch web pages using `requests.get()`.
- Key concepts:
  - Parsing HTML structure with `BeautifulSoup()`
  - Finding elements using `.find()`, `.find_all()`
  - Extracting text, attributes, and nested elements
  - Navigating DOM tree efficiently
- **Ethics:** Understanding robots.txt, respecting rate limits, and checking website ToS.

#### **API Data Extraction**

- **RESTful APIs:** Understanding endpoints, HTTP methods (GET, POST), and response formats.
- Extracting data using `requests.get()` and parsing JSON responses.
- Handling API keys and authentication headers.
- Working with pagination for large datasets.
- Error handling with try-except blocks for failed requests.
- Popular APIs: OpenWeather, NewsAPI, Twitter API, GitHub API, etc.

#### **Understanding Your Data**

- **Data Profiling:** Using `.info()`, `.describe()`, `.dtypes` to understand structure.
- **Statistical Summary:** Mean, median, std deviation, min/max values.
- **Distribution Analysis:** Skewness, kurtosis, and data shape characteristics.
- **Data Quality Checks:**
  - Missing values percentage
  - Duplicate records detection
  - Outlier identification using IQR method
  - Data type consistency validation
- **Correlation Analysis:** Using `corr()` to understand feature relationships.
- **Target Variable Analysis:** Understanding class distribution in classification problems.

**Key Insights:**  
Web scraping and APIs unlock vast data sources, while understanding your data prevents garbage-in-garbage-out scenarios. A deep understanding of data characteristics guides better preprocessing and model selection decisions.

![](./ASSETS/ml33.png)
![](./ASSETS/ml34.png)
![](./ASSETS/ml35.png)
![](./ASSETS/ml36.png)
![](./ASSETS/ml37.png)
![](./ASSETS/ml38.png)

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)
- [Krish Naik Web Scraping Tutorial](https://youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe)

### **Day 8: Univariate Analysis in Exploratory Data Analysis**

**Date:** 2025-12-20  
**Day:** Day 8  
**Topic:** Univariate Analysis

**What I Learned Today:**

- Univariate analysis focuses on **one variable at a time**.
- Helps understand distribution, central tendency, spread, and outliers.
- Essential before bivariate and multivariate analysis.

#### **Numerical Variables**
- Used `sns.histplot()`, `sns.displot()`, `sns.kdeplot()`
- Interpreted mean, median, skewness
- Used `stat='density'` and `stat='probability'`

#### **Categorical Variables**
- Used `sns.countplot()` and `value_counts()`
- Analyzed class imbalance
- Differentiated categories using `palette`

**Key Insights:**  
Univariate analysis builds strong intuition about individual features and directly impacts preprocessing and model performance.

![](./ASSETS/ml37.png)
![](./ASSETS/ml38.png)
![](./ASSETS/ml39.png)
![](./ASSETS/ml40.png)
![](./ASSETS/ml41.png)

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)

---
---

### **Day 9: Multivariate Analysis & Pandas Profiling**

**Date:** 2025-12-25  
**Day:** Day 9  
**Topic:** Multivariate Analysis & Pandas Profiling

**What I Learned Today:**  

- Multivariate analysis explores relationships between multiple variables.
- Visualized correlations using `sns.heatmap`, `pairplot`.
- Applied **Pandas Profiling** for automatic EDA reports with summary statistics, missing values, distributions, correlations, and sample data.
- Identified multicollinearity and feature interactions to prepare for ML models.
- Saved profiling reports as `output.html` for comprehensive inspection.

**Key Insights:**  
Multivariate analysis combined with profiling automates insights, highlights complex feature relationships, and guides preprocessing decisions.

![](./ASSETS/ml42.png)
![](./ASSETS/ml43.png)
![](./ASSETS/ml44.png)
![](./ASSETS/ml45.png)
![](./ASSETS/ml46.png)
![](./ASSETS/ml47.png)
![](./ASSETS/ml48.png)
![](./ASSETS/ml49.png)
![](./ASSETS/ml50.png)
![](./ASSETS/ml51.png)
![](./ASSETS/ml52.png)
![](./ASSETS/ml53.png)
![](./ASSETS/ml54.png)
![](./ASSETS/ml55.png)

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)

### **Day 10: Feature Engineering & Feature Scaling**  

**Date:** 2025-12-26  
**Day:** Day 10  
**Topic:** Feature Engineering Principles in Machine Learning, Standardization & Types of Normalization  

**What I Learned Today:**  

- **Feature Engineering Principles:**  
  - Selecting relevant features and transforming raw data to improve model performance.  
  - Creating new features from existing data to capture important patterns.  
  - Handling missing values, categorical encoding, and reducing multicollinearity.  

- **Feature Scaling:**  
  - **Standardization:** Transforming features to have **mean = 0** and **standard deviation = 1**.  
  - **Normalization:** Scaling features to a specific range, commonly **[0, 1]** or **[-1, 1]**.  
  - Types of normalization: **Min-Max scaling, Max-Abs scaling, and Robust scaling** for handling outliers.  

- Applied scaling techniques on the dataset to prepare for machine learning models.  
- Explored feature relationships and their impact on model learning.  
- Visualized scaled vs unscaled data distributions to understand transformations.  

**Key Insights:**  
Feature engineering and scaling are crucial preprocessing steps that directly affect model accuracy, convergence, and generalization. Choosing the right scaling method depends on the algorithm and data distribution.  

![](./ASSETS/ml56.jpeg)  
![](./ASSETS/ml57.jpeg)  
![](./ASSETS/ml58.jpeg)  
![](./ASSETS/ml59.jpeg)  
![](./ASSETS/ml60.png)  
![](./ASSETS/ml61.png)  
![](./ASSETS/ml62.png)  
![](./ASSETS/ml63.png)  
![](./ASSETS/ml64.png)  
![](./ASSETS/ml65.png)  
![](./ASSETS/ml66.png)  
![](./ASSETS/ml67.png)  
![](./ASSETS/ml68.png)  
![](./ASSETS/ml69.png)  
![](./ASSETS/ml70.png)  
![](./ASSETS/ml71.png)  
![](./ASSETS/ml72.png)  
![](./ASSETS/ml73.png)  
![](./ASSETS/ml74.png)  
![](./ASSETS/ml75.png)  
![](./ASSETS/ml76.png)  
![](./ASSETS/ml77.png)  
![](./ASSETS/ml78.png)  
![](./ASSETS/ml79.png)  
![](./ASSETS/ml80.png)  
![](./ASSETS/ml81.png)  

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)
---


### **Day 11: Encoding Categorical Labels**

**Date:** 2025-12-27  
**Day:** Day 11  
**Topic:** Encoding Categorical Labels using Imputer, Ordinal Encoder & One-Hot Encoder  

**What I Learned Today:**  

- **Handling Missing Categorical Data:**  
  - Used **SimpleImputer** to fill missing categorical values using strategies like `most_frequent`.  
  - Ensured categorical columns had no missing values before encoding.

- **Ordinal Encoding:**  
  - Applied **OrdinalEncoder** for categorical features with an inherent order.  
  - Explicitly defined category order to maintain consistency and meaning.  
  - Useful for features where relative ranking matters.

- **One-Hot Encoding:**  
  - Used **OneHotEncoder** to convert nominal categorical variables into binary vectors.  
  - Applied `drop='first'` to avoid dummy variable trap.  
  - Transformed categorical features into model-friendly numerical format.

- **ColumnTransformer:**  
  - Combined imputing and encoding steps into a single preprocessing pipeline.  
  - Applied different transformations to different columns efficiently.  

**Key Insights:**  
Proper encoding of categorical variables is essential for machine learning models to interpret non-numeric data correctly. Choosing between ordinal and one-hot encoding depends on whether the categorical feature has an inherent order.

![](./ASSETS/ml82.png)  
![](./ASSETS/ml83.png)  
![](./ASSETS/ml84.png)  
![](./ASSETS/ml85.png)  
![](./ASSETS/ml86.png)  
![](./ASSETS/ml87.png)  
![](./ASSETS/ml88.png)  
![](./ASSETS/ml89.png)  
![](./ASSETS/ml90.png)  
![](./ASSETS/ml91.png)  
![](./ASSETS/ml92.png)  
![](./ASSETS/ml93.png)  
![](./ASSETS/ml94.png)  
![](./ASSETS/ml95.png)  
![](./ASSETS/ml96.png)  
![](./ASSETS/ml97.png)  
![](./ASSETS/ml98.png)  
![](./ASSETS/ml99.png)  
![](./ASSETS/ml100.png)  

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)

---

### **Day 12: Introduction to Scikit-Learn Pipelines**

**Date:** 2025-12-28  
**Day:** Day 12  
**Topic:** Importance of Scikit-Learn Pipelines in Machine Learning Projects  

**What I Learned Today:**  

- **Introduction to Pipelines:**  
  - Learned what a **Scikit-learn Pipeline** is and why it is essential in machine learning workflows.  
  - Understood how pipelines chain preprocessing steps and models into a single object.

- **Avoiding Data Leakage:**  
  - Learned how pipelines prevent data leakage by ensuring preprocessing is applied only on training data during cross-validation.  
  - Ensured consistent transformations for both training and test datasets.

- **Clean & Maintainable Workflow:**  
  - Pipelines make machine learning code **cleaner, modular, and easier to debug**.  
  - Simplifies experimentation by allowing easy replacement of steps.

- **Compatibility with GridSearchCV:**  
  - Learned how pipelines work seamlessly with **GridSearchCV** for hyperparameter tuning.  
  - Understood that pipelines allow safe tuning of both preprocessing and model parameters together.

**Key Insights:**  
Scikit-learn pipelines are a best practice for building robust machine learning systems. They help maintain consistency, avoid common pitfalls like data leakage, and make models easier to tune, validate, and deploy in real-world projects.

![](./ASSETS/ml101.png)  
![](./ASSETS/ml102.png)  
![](./ASSETS/ml103.png)  
![](./ASSETS/ml104.png)  
![](./ASSETS/ml105.png)  
![](./ASSETS/ml106.png)  
![](./ASSETS/ml107.png)  
![](./ASSETS/ml108.png)  

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)

### **Day 13: Feature Transformation Techniques**

**Date:** 2025-12-29  
**Day:** Day 13  
**Topic:** Function Transformer, Log Transformer, and Box-Cox Transformer in Machine Learning  

**What I Learned Today:**  

- **Function Transformer:**  
  - Learned about the **FunctionTransformer** in Scikit-learn, which allows wrapping custom functions (like lambda or predefined) into pipelines for easy application on data.  
  - It's useful for applying arbitrary transformations without creating custom classes.

- **Log Transformer:**  
  - Explored the log transformer (e.g., using np.log or np.log1p) to handle right-skewed data distributions.  
  - It helps in stabilizing variance and making features more normally distributed, improving model performance on algorithms that assume normality.

- **Box-Cox Transformer:**  
  - Understood the Box-Cox transformation, a power transform that finds the optimal lambda to normalize data and reduce skewness.  
  - It's particularly effective for positive-valued data and can be integrated into pipelines for automated preprocessing.

**Key Insights:**  
These transformation techniques are crucial for preprocessing skewed features in machine learning pipelines. By applying FunctionTransformer with log or Box-Cox methods, we can enhance data normality, reduce the impact of outliers, and boost the accuracy of models like logistic regression during cross-validation and evaluation.

![](./ASSETS/ml109.png)  
![](./ASSETS/ml110.png)  
![](./ASSETS/ml111.png)  
![](./ASSETS/ml112.png)  
![](./ASSETS/ml113.png)  
![](./ASSETS/ml114.png)  
![](./ASSETS/ml115.png)  
![](./ASSETS/ml116.png)  
![](./ASSETS/ml117.png)  
![](./ASSETS/ml118.png)  
![](./ASSETS/ml119.png)  
![](./ASSETS/ml120.png)  
![](./ASSETS/ml121.png)  
![](./ASSETS/ml122.png)  
![](./ASSETS/ml123.png)  
![](./ASSETS/ml124.png)  
![](./ASSETS/ml125.png)  

**Resources Used Today:**  
- [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw)


<div id="bottom"></div>
<div align="center">
    <a href="#top" title="Jump to the top">
        <img src="https://img.shields.io/badge/▲_Jump_to_Top-0D1117?style=for-the-badge&logoColor=white&labelColor=161B22" alt="Jump to Top" />
    </a>
</div>

---

## Daily Progress Tracker

| Days | Date | Topics | Resources |
|----|------|--------|-----------|
| Day 1 | 2025-12-08 | Intro to ML | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) |
| Day 2 | 2025-12-09 | NumPy & Pandas | [Krish Naik ML Playlist](https://youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe) |
| Day 3 | 2025-12-10 | Visualization | [CampusX Visualization](https://youtu.be/3Xc3CA655Y4) • [Krish Naik Visualization](https://youtu.be/0P7QnIQDBJY) |
| Day 4 | 2025-12-12 | EDA | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) |
| Day 5 | 2025-12-13 | OOP | [Krish Naik ML Playlist](https://youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe) |
| Day 6 | 2025-12-14 | Data Manipulation | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) |
| Day 7 | 2025-12-15 | Web Scraping, APIs & Data Understanding | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) • [Krish Naik Web Scraping](https://youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe) |
| Day 8 | 2025-12-20 | Univariate Analysis | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) |
| Day 9 | 2025-12-25 | Multivariate & Pandas Profiling | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) |
| Day 10 | 2025-12-26 | Feature Engineering, Standardization & Types of Normalization | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) |
| Day 11 | 2025-12-27 | Encoding Categorical Labels | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) |
| Day 12 | 2025-12-28 | Introduction to Scikit-Learn Pipelines | [CampusX – 100 Days of ML](https://youtu.be/ZftI2fEz0Fw) |
| Day 13 | 2025-12-29 | Feature Transformation Techniques | [CampusX – 100 Days of ML ](https://youtu.be/ZftI2fEz0Fw) |
---