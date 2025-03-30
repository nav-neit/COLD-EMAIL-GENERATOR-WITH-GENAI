# COLD-EMAIL-GENERATOR-WITH-GENAI

A streamlined solution for tech service companies to generate personalized cold emails based on job postings, using Generative AI.

## Problem Statement

Tech service companies need to send targeted cold emails to potential clients for outsourcing work. This application automates the process by:
1. Extracting job descriptions from client career portals
2. Creating personalized, relevant emails based on the extracted information
3. Matching company portfolio examples with job requirements



1. **Data Extraction**: Uses LangChain Framework to extract text from career pages
2. **Information Processing**: Llama 3.1 extracts job details (roles, skills) into JSON format
3. **Portfolio Matching**: ChromaDB fetches relevant portfolio links based on job skills
4. **Email Generation**: LLM creates a personalized cold email using job details and portfolio links

## Technologies Used

- **LLM**: Llama 3.3 70B, accessed via GroqCloud for fast inference
- **Vector Database**: ChromaDB (open-source)
- **Framework**: LangChain for working with LLMs
- **UI**: Streamlit for a simple web interface
- **Data Processing**: Custom text processing utilities

## Setup Instructions

### Prerequisites
- Python 3.8+
- API key from GroqCloud
- Portfolio data in CSV format

### Installation

```bash
# Clone the repository
git clone https://github.com/nav-neit/COLD-EMAIL-GENERATOR-WITH-GENAI.git
cd COLD-EMAIL-GENERATOR-WITH-GENAI

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your API key
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

### Prepare Portfolio Data

Create a CSV file at `app/resource/my_portfolio.csv` with columns:
- `Techstack`: List of technologies/skills
- `Links`: Portfolio links showcasing these skills

### Running the Application

```bash
streamlit run app/main.py
```

## Usage

1. Enter the URL of a job posting from a client's career portal
2. Click "Submit"
3. The application will:
   - Extract job details (role, experience, skills)
   - Match relevant portfolio links
   - Generate a personalized cold email for outreach
4. Review and use the generated email for your outreach campaigns

## Project Structure

```
COLD-EMAIL-GENERATOR-WITH-GENAI/
│
├── app/
│   ├── chains.py       # LLM chain implementations for extraction and email generation
│   ├── main.py         # Streamlit UI and main application logic
│   ├── portfolio.py    # ChromaDB setup and portfolio management
│   ├── utils.py        # Text cleaning utilities
│   └── resource/       # Resource files
│       └── my_portfolio.csv   # Your portfolio data
│
├── vectorstore/        # ChromaDB persistent storage
├── .env                # Environment variables (API keys)
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.