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

---