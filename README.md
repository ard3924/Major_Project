# Android Malware Analysis and Detection using Machine Learning

This project is a web-based application designed to detect whether an Android application is malicious or benign based on the permissions it requests. It utilizes pre-trained machine learning models to provide real-time predictions through a user-friendly interface.

## 🚀 Features

- **Web-Based Interface**: An intuitive and responsive UI built with Flask and Bootstrap.
- **Permission-Based Analysis**: Classifies Android applications by analyzing the permissions they require.
- **Multiple ML Models**: Supports predictions from different trained models, including `LogisticRegression` and `ExtraTreeClassifier`.
- **Interactive Prediction**: Users can manually select permissions via a form to get an instant prediction.
- **Result Visualization**: Displays the prediction result clearly and provides an option to download the results as a PDF.
- **Performance Metrics**: Includes static pages to showcase model performance and comparison charts.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Libraries**: Bootstrap, jQuery, Owl Carousel, Google Charts

## 📂 Project Structure

```
Malware analysis and detection/
├── app.py                      # Main Flask application
├── logic_malware.pkl           # Pre-trained Logistic Regression model
├── ExtraTree_malware.pkl       # Pre-trained Extra Trees Classifier model
├── templates/
│   ├── index.html              # Home page
│   ├── login.html              # Login page (static)
│   ├── upload.html             # Dataset upload page
│   ├── preview.html            # Data preview page
│   ├── prediction.html         # Main prediction form
│   ├── result.html             # Displays the prediction result
│   ├── performance.html        # Static performance metrics page
│   └── chart.html              # Static model comparison chart page
└── static/
    ├── assets/
    │   ├── css/
    │   ├── images/
    │   └── js/
    └── vendor/
        ├── bootstrap/
        └── jquery/
```

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd "Malware analysis and detection"
```

### 2. Create a Virtual Environment (Recommended)

It's good practice to create a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Create a `requirements.txt` file with the following content:

```
Flask
pandas
numpy
scikit-learn
matplotlib
seaborn
```

Then, install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Execute the `app.py` file to start the Flask development server.

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

## 📖 How to Use

1.  **Login**: Navigate to the `/login` page. Use the hardcoded credentials `admin` for both username and password to proceed.
2.  **Upload (Optional)**: The `/upload` page allows you to upload a CSV dataset, which is then displayed on the `/preview` page.
3.  **Predict**:
    - Go to the `/prediction` page.
    - You will see a form with a list of Android permissions.
    - For each permission, select "Yes" if the app requires it, and "No" otherwise.
    - Choose the machine learning model you want to use for the prediction (`ExtraTreeClassifier` or `LogisticRegression`).
    - Click the **Predict** button.
4.  **View Results**: You will be redirected to the `/result` page, which shows the inputs you provided and the final prediction (`Malware` or `Benign`). You can also download these results as a PDF.

## 📈 Future Improvements

- **Real User Authentication**: Replace the hardcoded login with a proper database-backed authentication system.
- **APK Analysis**: Allow users to upload an `.apk` file directly. The backend would then automatically extract the required permissions and run the prediction.
- **Dynamic Training**: Implement the model training logic to use the dataset uploaded by the user.
- **Enhanced Visualizations**: Make the performance and chart pages dynamic based on real-time model evaluations.

---