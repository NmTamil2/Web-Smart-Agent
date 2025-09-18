# 🌐 Web Smart Agent 🤖✨

This project is a simple **AI-powered web content extraction agent** that uses [⚡ Pydantic AI](https://docs.pydantic.dev/latest/ai/), [🔌 MCP](https://modelcontextprotocol.io/), and [🧠 OpenAI](https://platform.openai.com/) APIs.  
It loads environment variables, runs an MCP fetch server, and queries webpages for **structured information**.

---

## 🚀 Features
- 🔑 Loads secrets from `.env` file (`OPENAI_API_KEY`)
- 🤖 Uses `pydantic_ai.Agent` with `gpt-4o` (can be switched to Groq models)
- 🌍 Integrates **MCP server** for fetching webpage content
- 📊 Extracts structured information (like cricket stats from Cricbuzz)
- ⚡ Runs asynchronously with Python `asyncio`

---

## 📂 Project Structure
web-smart-agent/
│── main.py # 📝 Main entry point
│── requirements.txt # 📦 Python dependencies
│── .env # 🔑 Environment variables (not committed to git)
│── .gitignore # 🚫 Ignore files like .env, env/
│── env/ # 🐍 (optional) local virtual environment




---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Web-Smart-Agent.git
cd Web-Smart-Agent


2️⃣ Create a virtual environment
python -m venv env
source env/bin/activate   # On Linux/Mac 🐧
env\Scripts\activate      # On Windows 💻

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file in the project root:
OPENAI_API_KEY=your_openai_api_key_here
# GROQ_API_KEY=your_groq_api_key_here   # (optional)


5️⃣ Run the project
python main.py

🖥️ Example Output

The script will fetch live cricket match data from Cricbuzz 🏏 and extract bowler economy rates into a table:
Bowler       Overs   Runs   Wickets   Economy
Bumrah       10      45     2         4.5
Anderson     8       39     1         4.9
...
