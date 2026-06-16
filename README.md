# 🤝 AI Negotiation Studio

AI Negotiation Studio is an intelligent negotiation simulation platform that enables users to practice, analyze, and improve negotiation skills through AI-powered conversations.

The system combines Large Language Models (Groq Llama 3.1), negotiation analytics, AI coaching, transcript management, and automated report generation to create an interactive negotiation training environment.

---

## 🚀 Features

### 💬 AI Negotiation Simulator

- Real-time AI-powered negotiation conversations
- Multiple negotiation scenarios
- Dynamic personality-driven responses
- Context-aware conversation memory
- Intelligent negotiation flow management

### 🧠 AI Coach

- Post-negotiation feedback
- Strength identification
- Weakness detection
- Actionable improvement suggestions
- LLM-powered negotiation analysis

### 📊 Negotiation Analytics

- Negotiation Score
- Efficiency Rating
- Quality Assessment
- Conversation Duration
- Total Negotiation Rounds
- Outcome Tracking

### 📄 Automated Reporting

Generate professional PDF reports containing:

- Negotiation Summary
- Scenario Information
- Participant Persona
- Outcome Analysis
- AI Coach Feedback
- Analytics Dashboard
- Final Verdict
- Full Conversation Transcript

### 🎨 Modern Streamlit Interface

- Chat-style interaction
- Multi-tab dashboard
- Analytics panel
- AI Coach panel
- Report generation panel
- Professional dark theme

---

## 🏗️ System Architecture

```text
AI-NEGOTIATION-SIMULATOR
│
├── agent/
│   ├── negotiation_agent.py
│   ├── memory.py
│   ├── state_machine.py
│   └── ai_response_generator.py
│
├── analytics/
│   └── negotiation_analytics.py
│
├── coach/
│   └── llm_coach.py
│
├── nlp/
│   ├── ai_intent_classifier.py
│   └── groq_engine.py
│
├── personality/
│   └── personalities.py
│
├── prompts/
│   ├── prompt_engine.py
│   └── response_templates.py
│
├── reporting/
│   └── report_generator.py
│
├── scenarios/
│   └── scenario_manager.py
│
├── streamlit_app/
│   ├── app.py
│   ├── chat_ui.py
│   ├── coach_panel.py
│   ├── metrics_panel.py
│   ├── theme.py
│   └── ui.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## 🛠️ Technology Stack

### Frontend

- Streamlit

### Backend

- Python

### AI & NLP

- Groq API
- Llama 3.1 8B Instant
- Prompt Engineering

### Analytics

- Custom Negotiation Metrics
- State-Based Evaluation

### Reporting

- ReportLab
- PDF Generation

### Data Processing

- Pandas

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Negotiation-Studio.git

cd AI-Negotiation-Studio
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Environment File

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

### 4. Run Application

```bash
streamlit run streamlit_app/app.py
```

---

## 🎯 Example Workflow

1. Select a negotiation scenario
2. Choose a negotiator personality
3. Start negotiating with the AI agent
4. Receive dynamic AI responses
5. View analytics and coaching insights
6. Generate a professional PDF report
7. Download and review performance

---

## 📈 Sample Analytics

The platform evaluates negotiations using:

- Total Rounds
- Negotiation Duration
- Negotiation Score
- Efficiency Rating
- Quality Rating
- Final Outcome

---

## 📑 Generated Report Contents

Each generated report includes:

- Report Summary
- Negotiation Analytics
- AI Coach Analysis
- Final Verdict
- Complete Conversation Transcript

---

## 🔐 Environment Variables

| Variable | Description |
|-----------|------------|
| GROQ_API_KEY | Groq API Key for LLM responses |

---

## 🎓 Academic Use

This project was developed as part of an academic study in:

- Artificial Intelligence
- Natural Language Processing
- Human-AI Interaction
- Negotiation Support Systems

---

## 👨‍💻 Author

**Sargam Hemnani**

M.Tech Project

AI Negotiation Studio

---

## 📜 License

This project is intended for educational and research purposes.