# 📰 News Research Tool

## 📌 Project Overview

News Research Tool is a Python and Streamlit based application that allows users to search for the latest news articles based on a topic.

The application uses NewsAPI to fetch news articles and displays the article title, source, publication date, summary and original article link.

The project also includes LangChain and OpenAI configuration for AI-powered summarization.

Since OpenAI API credits are currently unavailable, the application uses the article description as a free fallback summary.

---

## ✨ Features

* 🔎 Search news by any topic
* 📰 Fetch latest news articles using NewsAPI
* 📄 Display article title and source
* 📅 Display publication date
* 📝 Display article summary
* 🔗 Provide original article URL
* 🖼️ Display article images when available
* 🆓 Free fallback summary when OpenAI is unavailable
* 🖥️ Interactive Streamlit interface
* 🔄 Recent search history

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NewsAPI
* LangChain
* OpenAI API
* python-dotenv

---

## 📁 Project Structure

```text
News_Research_Tool/
│
├── .env
├── .gitignore
├── app.py
├── langchain_config.py
├── news_fetcher.py
├── summarizer.py
├── README.md
├── requirements.txt
└── venv/
```

### File Description

**app.py**
Main Streamlit application and user interface.

**news_fetcher.py**
Fetches news articles from NewsAPI.

**summarizer.py**
Processes article summaries and provides a fallback summary when AI summarization is unavailable.

**langchain_config.py**
Contains LangChain and OpenAI configuration.

**.env**
Stores API keys and environment variables.

**requirements.txt**
Contains required Python packages.

**.gitignore**
Prevents sensitive and unnecessary files from being uploaded.

---

## ⚙️ Requirements

Before running the project, install:

* Python 3.x
* pip
* NewsAPI key
* VS Code

OpenAI API access is optional for the current fallback version.

---

## 🚀 Installation

### 1. Create Virtual Environment

Open the VS Code terminal and run:

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project folder.

Add:

```env
NEWS_API_KEY=your_newsapi_key_here
```

If OpenAI integration is used, you can also add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### ⚠️ Security

Never share your real API keys publicly.

The `.env` file should remain private.

---

## ▶️ How to Run

### Test NewsAPI

Run:

```bash
python news_fetcher.py
```

Enter a topic such as:

```text
Artificial Intelligence
```

---

### Test Summarizer

Run:

```bash
python summarizer.py
```

Enter:

```text
Artificial Intelligence
```

The application will retrieve news articles and display summaries.

---

### Run Streamlit Application

Run:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

in your browser.

---

## 🔄 Application Workflow

```text
User enters news topic
        ↓
Streamlit Application
        ↓
NewsAPI
        ↓
News Articles
        ↓
Article Processing
        ↓
Summarization
        ↓
AI Summary / Free Fallback
        ↓
Results displayed
```

---

## 🤖 LangChain + OpenAI Integration

The project includes LangChain and OpenAI configuration for AI-powered article summarization.

The intended workflow is:

```text
News Article
     ↓
LangChain
     ↓
OpenAI Model
     ↓
Generated Summary
     ↓
Streamlit
```

However, OpenAI API usage requires available API credits.

Therefore, the current project uses a fallback method.

---

## 🆓 Free Fallback Mode

When OpenAI API summarization is unavailable, the application uses the article description provided by NewsAPI.

```text
Article
   ↓
OpenAI unavailable
   ↓
Use article description
   ↓
Display summary
```

This allows the project to continue working without paid OpenAI API usage.

---

## 📸 Screenshots

Screenshots of the Streamlit application can be added here.

Recommended screenshots:

1. Home page
2. News search results
3. Article summary
4. Recent search history

Example:

```text
![News Research Tool](screenshots/news_research_tool.png)
```

---

## 🔮 Future Enhancements

Possible future improvements:

1. Full AI-powered summarization
2. User authentication
3. Advanced news filters
4. Date-based filtering
5. Sentiment analysis
6. Keyword extraction
7. Multi-language summaries
8. PDF/CSV export
9. Database integration
10. Cloud deployment

---

## 🧪 Testing

The project was tested using the following topic:

```text
Artificial Intelligence
```

The application successfully:

* Retrieved news articles
* Displayed article information
* Displayed article summaries
* Displayed source information
* Displayed article URLs
* Used fallback summaries when OpenAI was unavailable

---

## ⚠️ Important Notes

* A valid NewsAPI key is required.
* Internet connection is required.
* OpenAI API credits are not required for the current fallback mode.
* Never share your API keys publicly.
* News results depend on the NewsAPI response.

---

## 🎯 Conclusion

The News Research Tool demonstrates the use of Python, Streamlit, NewsAPI, LangChain and OpenAI integration to create a simple news research application.

The fallback mechanism allows the application to remain functional even when OpenAI API credits are unavailable.

---

## 👩‍💻 Author

**Ankita Babar**

Data Science / Data Analysis Project

---

## 📄 License

This project is created for educational and project demonstration purposes.
