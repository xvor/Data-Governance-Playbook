# 📋 Data Governance Playbook Generator

A Claude-powered tool that generates tailored 90-day data governance action plans mapped to **DCAM** (EDM Council) and **DAMA DMBOK2** — the two leading frameworks for enterprise data management maturity.

> Built as a portfolio project demonstrating applied AI governance product thinking.  
> Read the full write-up on [Medium →](https://medium.com/@xvor)

---

## What it does

You provide four inputs:
- **Organisation type** — enterprise, mid-size, scale-up, or public sector
- **Industry** — financial services, industrial/energy, healthcare, technology, etc.
- **Current DCAM maturity level** — from "Not Initiated" to "Optimising"
- **Biggest pain point** — data quality, regulatory risk, no ownership, AI readiness, silos, or metadata

The tool generates a structured 90-day playbook with:
- **3 phases** of 30 days each, each with a distinct theme and objective
- **3 actions per phase** — specific, verb-led, and grounded in your industry context
- **DCAM component tag** — maps each action to one of DCAM's 8 capability components
- **DMBOK knowledge area tag** — cross-references DAMA DMBOK2's 10 practice areas
- **Success signal** — a concrete, observable definition of "done" for each action
- **Effort level** and **key stakeholders** for each action

---

## Why DCAM + DMBOK?

| Framework | Owner | Focus |
|---|---|---|
| **DCAM** | EDM Council | *Capability assessment* — how mature is your data management? |
| **DMBOK2** | DAMA International | *Practice guidance* — what does good data management look like? |

They are complementary: DCAM tells you *where you are*, DMBOK tells you *what to do*. Most enterprise Data Office programmes reference both. Knowing them is table stakes for Data Office Leader, Chief Data Officer, and Data Governance PM roles.

See `framework_reference.py` for a full breakdown of both frameworks with component descriptions, key outputs, and DCAM→DMBOK mappings.

---

## Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/xvor/data-governance-playbook-generator
cd data-governance-playbook-generator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Anthropic API key
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 4. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Project structure

```
data-governance-playbook-generator/
├── app.py                   # Streamlit application (main entry point)
├── framework_reference.py   # Standalone DCAM + DMBOK reference module
├── PRODUCT_SPEC.md          # Product spec — personas, metrics, V1 vs V2 decisions
├── requirements.txt
├── .env.example
└── README.md
```

---

## Framework reference

Run the reference module standalone to explore both frameworks:

```bash
python framework_reference.py
```

This prints:
- DCAM's 5 maturity levels and 8 components with descriptions
- DMBOK2's 10 knowledge areas
- The DCAM → DMBOK cross-mapping used by the playbook generator

---

## Design decisions

**Why Streamlit?**  
Fast to build, easy to share, and lets the framework logic stay front and centre rather than getting buried in frontend code. The focus is on the governance thinking, not the UI.

**Why 90 days?**  
The 30/60/90 structure mirrors how real Data Office programmes are launched — diagnose and align in the first month, implement foundational capabilities in the second, and start measuring and scaling in the third.

**Why DCAM maturity as an input?**  
An organisation at "Not Initiated" needs a completely different playbook than one at "Defined". The maturity level is the single most important variable in determining what actions will actually land. Generic governance advice ignores this and fails.

**Why not a chatbot?**  
Chatbots are useful for exploration. This is a *decision support tool* — structured inputs, structured outputs, designed to be shared with a team and used as a working document. The JSON download reinforces this.

---

## Sample output

```json
{
  "playbook_title": "Building Data Trust in Financial Services — From Conceptual to Controlled",
  "executive_summary": "This playbook establishes the governance foundations needed to move a mid-size bank from awareness to action on data quality. Phase 1 aligns leadership and maps the data landscape. Phase 2 puts ownership and quality rules in place. Phase 3 operationalises measurement and scales adoption.",
  "phases": [
    {
      "phase_number": 1,
      "theme": "Diagnose and Align",
      "objective": "Secure leadership sponsorship and produce a clear picture of the current data landscape",
      "actions": [...]
    }
  ]
}
```

---

## Related projects

- [**AI Risk Lens**](https://github.com/xvor/ai-risk-lens) — Maps AI features to NIST AI RMF tiers and EU AI Act classifications
- [**Skill Trust Engine**](https://github.com/xvor/skill-trust-engine) — Evaluates AI agent skill risk profiles across four governance dimensions

---

## Author

**Vijay** · Staff TPM → AI Governance PM  
CIPT · CISSP · 20 years at the intersection of AI, privacy, and compliance

[GitHub](https://github.com/xvor) · [Medium](https://medium.com/@xvor) · [LinkedIn](https://linkedin.com/in/xvor)

---

## License

MIT
