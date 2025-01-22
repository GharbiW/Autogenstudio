# Autogenstudio
This repository showcases hands-on projects using AutoGenStudio 2.0 to simulate a marketing agency with multi-agent Large Language Models (LLMs). It includes detailed workflows, essential skills, and a collection of useful tools designed to streamline digital marketing tasks. 

Here’s a **complete README file** tailored for your GitHub project, integrating all the aspects of your empirical analysis, methodology, workflows, agents, and technical setup. This version is concise yet comprehensive and aligned with professional GitHub standards.  

---

# **Multi-Agent LLM Framework for Marketing Automation**  

This repository explores the implementation of a **multi-agent LLM framework** for simulating a marketing agency's operations. The project evaluates how advanced frameworks like **AutoGen Studio** and models such as **OpenAI 4-0 Mini** and **Mistral** enable agents to collaborate dynamically, solve complex tasks, and deliver high-quality marketing outputs.  

---

## **Table of Contents**  
1. [Project Overview](#project-overview)  
2. [Methodology](#methodology)  
3. [Agent Roles and Workflow](#agent-roles-and-workflow)  
4. [Technical Setup](#technical-setup)  
5. [Skills Integration](#skills-integration)  
6. [Experimental Results](#experimental-results)  
7. [Usage Instructions](#usage-instructions)  
8. [Acknowledgments](#acknowledgments)  

---

## **Project Overview**  

This project aims to:  
- Test the capabilities of **AutoGen**, a multi-agent LLM framework, in simulating dynamic workflows within a virtual marketing agency.  
- Evaluate the collaboration and problem-solving efficiency of agents equipped with specialized roles and Python-based skills.  
- Optimize task decomposition and execution while maintaining cost efficiency and scalability.  

The framework is tested on various tasks, including landing page creation, content generation, sentiment analysis, and web development, within a structured yet adaptable workflow.  

---

## **Methodology**  

To conduct the experiments:  
- **Framework**: Used **AutoGen Studio**, a low-code platform, to configure dynamic workflows and deploy multi-agent systems.  
- **AI Models**: Leveraged **OpenAI 4-0 Mini** for cost-efficient task execution and **Mistral** for research-intensive operations.  
- **Workflow**: Developed a non-linear, task-specific workflow to ensure agents collaborate only when necessary, minimizing token consumption and enhancing precision.  
- **Challenges Addressed**: Reduced unnecessary interactions, optimized token usage, and ensured high-quality outputs across various scenarios.  

---

## **Agent Roles and Workflow**  

### **Agents**  
- **Creative Agent**: Generates strategies and guides workflows.  
- **Data Analysis Agent**: Processes raw data into actionable insights.  
- **Web Research Agent**: Collects relevant market data and trends.  
- **Content Creator**: Produces marketing copy and articles.  
- **Image Generator**: Designs visuals using DALL-E 3.  
- **Web Scrap and Social Media Scrap**: Extract data from websites and platforms.  

**Workflow Highlights**:  
- Agents collaborate dynamically based on task relevance.  
- Information flows systematically from supporting to primary agents, enabling seamless decision-making and execution by secondary agents.  

---
Here's the updated **Installation Steps** section with the **AutoGen Studio setup** and **requirements.txt details** included:  

---

## **Installation Steps**  

### **1. Clone the Repository**  
Start by cloning this repository:  
```bash  
git clone https://github.com/username/repo-name.git  
cd repo-name  
```  

### **2. Install AutoGen Studio**  
Download and set up **AutoGen Studio** from its official repository:  
```bash  
git clone https://github.com/microsoft/autogen.git  
cd autogen  
```  

### **3. Set Up a Virtual Environment**  
Create and activate a virtual environment to isolate dependencies:  
```bash  
python -m venv env  
source env/bin/activate  # macOS/Linux  
env\Scripts\activate     # Windows  
```  

### **4. Install Dependencies**  
Run the following command to install the necessary Python packages:  
```bash  
pip install -r requirements.txt  
```  

**Example requirements.txt File** (included in the repository):  
```text  
autogen-agentchat[lmm]~=0.2  
openai==1.36.1  
google-api-python-client  
selenium  
beautifulsoup4  
pytrends  
PyPDF2  
textblob  
pandas  
numpy  
tailwindcss  
react  
bootstrap  
```  

Ensure all dependencies are installed for proper execution of agents and skills.  

### **5. Add API Keys**  
Create a `.env` file in the root directory and configure your API keys:  
```bash  
OPENAI_API_KEY=your_openai_api_key  
GOOGLE_API_KEY=your_google_api_key  
GOOGLE_SEARCH_ENGINE_ID=your_google_search_engine_id  
YOUTUBE_API_KEY=your_youtube_api_key  
```  

Load the `.env` file in your Python scripts using `dotenv`:  
```bash  
pip install python-dotenv  
```  

### **6. Start AutoGen Studio**  
To launch AutoGen Studio, run:  
```bash  
python -m autogenstudio  
```  

AutoGen Studio will start a local server and open in your default web browser.  

### **7. Verify Skills Integration**  
Place all pre-built Python skills in the `skills/` directory and test them independently:  
```bash  
python skills/<skill_name>.py  
```  

---

This expanded section ensures all the required steps for installing **AutoGen Studio**, setting up dependencies, and integrating skills are clear and actionable.
---

## **Skills Integration**  

### **Available Skills**  
1. **Web Scraping**: Extract structured and unstructured data using Selenium and BeautifulSoup.  
2. **Google Trends API**: Fetch trending data for market analysis.  
3. **YouTube Transcript**: Retrieve transcripts and metadata from videos.  
4. **Image Generation**: Create visuals with OpenAI’s DALL-E 3.  
5. **Sentiment Analysis**: Evaluate emotional tones in content using TextBlob.  
6. **Content Analysis**: Process and classify text data.  
7. **PDF Handling**: Extract and save content from PDF files.  
8. **Web Development**: Utilize Tailwind CSS, ReactJS, and Bootstrap for creating landing pages.  

**Skill Execution**: Skills are pre-built Python files located in the `skills/` directory. Run them as standalone scripts or integrate them into workflows. Example:  
```python  
from skills.web_scraper import WebScraper  
scraper = WebScraper()  
data = scraper.scrape("https://example.com")  
print(data)  
```  

---

## **Usage Instructions**  

1. **Configure Agents**: Use AutoGen Studio to define workflows and assign roles to agents.  
2. **Run Tasks**: Deploy workflows by initiating task-specific simulations in the Studio.  
3. **Analyze Outputs**: Monitor results through logs and dashboards for performance evaluation.  

---
