
# 🔍 LLM GenAI Powered ATS Resume Analyzer

Welcome to the **ATS Resume Checker**! This tool leverages the power of **Large Language Models (LLM)** and **Generative AI (GenAI)** to review your resume based on specific job descriptions. Get a score out of 100 and discover which keywords are missing to make your resume ATS-compliant for tech jobs!


## 🔑 Setting Up Google API Key

This application requires a Google API key. Follow these steps to configure the environment variable securely:

1. **Duplicate the Sample Environment File**:  
   In the root directory of the project, locate the `.env_sample` file and make a copy of it, renaming the copy to `.env`:
   ```bash
   cp .env_sample .env
   ```

2. **Add Your Google API Key**:  
   Open the newly created `.env` file in a text editor and replace `YOUR_API_KEY_HERE` with your actual Google API key:
   ```plaintext
   GOOGLE_API_KEY="your_google_api_key"
   ```

3. **Save the `.env` File**:  
   Ensure the `.env` file is saved in the project’s root directory. This file will be automatically loaded at runtime to provide the Google API key securely.


## 🚀 Getting Started

Follow these steps to set up and run the application.

### 1. **Create a Virtual Environment**
   ```bash
   python3 -m venv .venv
   ```

### 2. **Activate the Virtual Environment**
   ```bash
   source .venv/bin/activate
   ```

### 3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

### 4. **Run the Streamlit Application**
   ```bash
   streamlit run app.py
   ```

## 🖥️ Application Interface

The interface is designed to be user-friendly and intuitive.

### Input Job Description
1. Paste the job description in the provided field.  
2. Upload your resume in PDF format.
 
![Screenshot 2024-10-24 at 11 48 41 PM](https://github.com/user-attachments/assets/e0dcbe97-af97-4d2b-b62b-2b4633a8b71a)
    
*This screenshot shows the job description input field and resume upload section.*

### Resume Analysis
Once the job description and resume are provided, the tool will analyze and highlight missing keywords and generate an ATS score.

![Screenshot 2024-10-24 at 11 49 46 PM](https://github.com/user-attachments/assets/da36ffcc-d530-465b-86ad-b9271585d93c)

*The app processes the resume using GenAI, providing feedback on alignment with the job description.*

### Analysis Results
The results page categorizes missing keywords by **Programming Languages**, **Tools and Software**, **Algorithms**, **Frameworks**, and **Other** relevant terms. It also displays the ATS score, showing how well your resume aligns with the job description.

![Screenshot 2024-10-24 at 11 50 09 PM](https://github.com/user-attachments/assets/32ebbf93-9086-4e76-80a3-0ff749bc9661)


*View categorized missing keywords and the ATS score for quick improvements.*

## 📦 Dependencies

- **streamlit**: for the interactive web app.
- **streamlit_lottie**: for animations.
- **PyPDF2**: for PDF text extraction.
- **google-generativeai**: for integrating generative AI.
- **python-dotenv**: for environment variables.
- **watchdog**: for file monitoring.


## 🌍 How to Contribute

1. Fork the repository.
2. Create a new branch for changes.
3. Submit a pull request.

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## 📬 Contact

For any questions or suggestions, please reach out at ashutoshdevpura@gmail.com.
