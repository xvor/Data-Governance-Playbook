"""
Data Governance Playbook Generator
Generates tailored 90-day data governance playbooks mapped to DCAM and DAMA-DMBOK2.
"""

import streamlit as st
import anthropic
import json
from typing import Optional

st.set_page_config(
    page_title="Data Governance Playbook Generator",
    page_icon="📋",
    layout="centered",
)

DCAM_COMPONENTS = [
    "Data Management Strategy",
    "Data Management Business Case",
    "Data Management Program and Funding",
    "Data Governance",
    "Data Architecture",
    "Data Quality Management",
    "Data Management Operations Risk and Control",
    "Analytics Management",
]

DMBOK_AREAS = [
    "Data Governance",
    "Data Architecture",
    "Data Modeling and Design",
    "Data Storage and Operations",
    "Data Security",
    "Data Integration and Interoperability",
    "Reference and Master Data",
    "Data Warehousing and Business Intelligence",
    "Metadata Management",
    "Data Quality",
]

MATURITY_LEVELS = {
    "Not Initiated": "No formal data governance capability exists. Data is managed ad hoc, ownership is unclear, and there are no policies or processes in place.",
    "Conceptual": "Awareness of data governance exists at leadership level, but nothing has been formalised. Champions may exist but lack mandate or budget.",
    "Developmental": "Some governance work is underway — perhaps a data catalogue pilot or quality initiative — but it is inconsistent and not enterprise-wide.",
    "Defined": "A formal governance framework exists, roles and responsibilities are documented, and processes are consistently applied across business units.",
    "Optimising": "Governance is measured, continuously improved, and tightly integrated with business outcomes. Data is treated as a strategic asset.",
}

ORG_TYPES = [
    "Large Enterprise (10,000+ employees)",
    "Mid-size Company (1,000–10,000 employees)",
    "Scale-up / Growth Stage (100–1,000 employees)",
    "Government / Public Sector",
]

INDUSTRIES = [
    "Financial Services / Banking / Insurance",
    "Industrial / Manufacturing / Energy",
    "Healthcare / Life Sciences / Pharma",
    "Technology / Software / AI",
    "Retail / Consumer / E-commerce",
    "Telecommunications",
    "Public Sector / Government",
]

PAIN_POINTS = [
    "Data quality and trust — teams don't trust the data they work with",
    "Regulatory & compliance risk — upcoming audits, GDPR, data residency obligations",
    "No clear data ownership — accountability for data assets is undefined",
    "AI / ML readiness — can't trust data to train or run models reliably",
    "Data silos — teams can't find or share data across the organisation",
    "Metadata & discoverability — no catalogue, no lineage, no definitions",
]

PHASE_COLORS = {
    1: {"bg": "#EEEDFE", "text": "#3C3489", "label": "Phase 1 — Days 1–30"},
    2: {"bg": "#E1F5EE", "text": "#085041", "label": "Phase 2 — Days 31–60"},
    3: {"bg": "#FAECE7", "text": "#993C1D", "label": "Phase 3 — Days 61–90"},
}

SYSTEM_PROMPT = """You are a senior data governance advisor with deep expertise in:
- DCAM (Data Management Capability Assessment Model) by the EDM Council
- DAMA DMBOK2 (Data Management Body of Knowledge, 2nd edition)
- Enterprise data strategy and data office programme design

You generate precise, opinionated, industry-specific 90-day governance playbooks.
Your recommendations reflect the maturity level and industry context provided. You avoid generic advice."""


def build_prompt(org: str, industry: str, maturity: str, pain: str) -> str:
    maturity_context = MATURITY_LEVELS.get(maturity, "")
    return f"""A client organisation needs a 90-day Data Governance Playbook.

CONTEXT:
- Organisation type: {org}
- Industry: {industry}
- Current DCAM maturity level: {maturity}
- Maturity description: {maturity_context}
- Biggest pain point: {pain}

Generate a 90-day playbook as 3 phases of 30 days, with exactly 3 actions per phase.

Each action must:
1. Be specific to the given industry and maturity level (not generic)
2. Address the pain point progressively across phases
3. Map to one DCAM component and one DMBOK knowledge area
4. Include a concrete success signal

DCAM components: {', '.join(DCAM_COMPONENTS)}
DMBOK areas: {', '.join(DMBOK_AREAS)}

Respond ONLY with valid JSON. No markdown, no backticks, no preamble.

{{
  "playbook_title": "short descriptive title",
  "executive_summary": "2-3 sentence summary of approach and outcomes",
  "phases": [
    {{
      "phase_number": 1,
      "theme": "short theme name",
      "objective": "one sentence describing what this phase achieves",
      "actions": [
        {{
          "action": "verb-led action title",
          "detail": "2-3 sentences on what to do, who leads it, and why it matters for this specific context",
          "success_signal": "what does done look like?",
          "dcam_component": "one DCAM component",
          "dmbok_area": "one DMBOK area",
          "effort": "Low|Medium|High",
          "stakeholders": ["stakeholder1", "stakeholder2"]
        }}
      ]
    }}
  ]
}}"""


def generate_playbook(org: str, industry: str, maturity: str, pain: str) -> Optional[dict]:
    try:
        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": build_prompt(org, industry, maturity, pain)}],
        )
        raw = message.content[0].text.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(raw)
    except json.JSONDecodeError as e:
        st.error(f"Failed to parse the generated playbook. Please try again. ({e})")
        return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None


def render_playbook(playbook: dict) -> None:
    st.markdown(f"## {playbook.get('playbook_title', '90-Day Data Governance Playbook')}")
    if summary := playbook.get("executive_summary"):
        st.info(f"**Executive summary:** {summary}")
    st.markdown("---")

    effort_emoji = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}

    for phase in playbook.get("phases", []):
        n = phase["phase_number"]
        c = PHASE_COLORS[n]
        st.markdown(
            f'<div style="background:{c["bg"]};padding:10px 16px;border-radius:8px;margin-bottom:4px">'
            f'<span style="color:{c["text"]};font-weight:600;font-size:13px">{c["label"]}</span>'
            f'<span style="color:{c["text"]};font-size:18px;font-weight:600;margin-left:12px">{phase["theme"]}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.caption(f"Objective: {phase.get('objective', '')}")
        st.markdown("")

        numerals = ["①", "②", "③"]
        for i, action in enumerate(phase.get("actions", [])):
            effort = action.get("effort", "Medium")
            with st.expander(f"{numerals[i]}  {action['action']}  {effort_emoji.get(effort, '')}", expanded=True):
                st.markdown(action["detail"])
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(
                        f'<span style="background:#EEEDFE;color:#3C3489;padding:3px 10px;border-radius:20px;font-size:12px">DCAM: {action["dcam_component"]}</span>',
                        unsafe_allow_html=True,
                    )
                with col2:
                    st.markdown(
                        f'<span style="background:#E1F5EE;color:#085041;padding:3px 10px;border-radius:20px;font-size:12px">DMBOK: {action["dmbok_area"]}</span>',
                        unsafe_allow_html=True,
                    )
                st.markdown("")
                st.markdown(f"✅ **Success signal:** {action.get('success_signal', '')}")
                if stakeholders := action.get("stakeholders"):
                    st.markdown(f"👥 **Stakeholders:** {', '.join(stakeholders)}")
        st.markdown("---")


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("### Framework reference")
        with st.expander("DCAM components", expanded=False):
            st.markdown("**EDM Council DCAM** — 8 capability components:")
            for c in DCAM_COMPONENTS:
                st.markdown(f"- {c}")
            st.markdown("[Learn more →](https://edmcouncil.org/frameworks/dcam/)")
        with st.expander("DMBOK knowledge areas", expanded=False):
            st.markdown("**DAMA DMBOK2** — 10 knowledge areas:")
            for a in DMBOK_AREAS:
                st.markdown(f"- {a}")
            st.markdown("[Learn more →](https://www.dama.org/cpages/body-of-knowledge)")
        with st.expander("Maturity levels", expanded=False):
            for level, desc in MATURITY_LEVELS.items():
                st.markdown(f"**{level}**")
                st.caption(desc)
        st.markdown("---")
        st.caption("Built by [xvor](https://github.com/xvor) · [Medium](https://medium.com/@xvor) · [LinkedIn](https://linkedin.com/in/xvor)")


def main() -> None:
    render_sidebar()
    st.title("📋 Data Governance Playbook Generator")
    st.markdown(
        "Generate a tailored 90-day data governance action plan mapped to "
        "**DCAM** (EDM Council) and **DAMA DMBOK2** — the two leading frameworks "
        "for enterprise data management maturity."
    )
    st.markdown("")

    with st.form("playbook_form"):
        col1, col2 = st.columns(2)
        with col1:
            org = st.selectbox("Organisation type", ORG_TYPES)
            maturity = st.selectbox("Current governance maturity", list(MATURITY_LEVELS.keys()), index=1)
        with col2:
            industry = st.selectbox("Industry", INDUSTRIES)
            pain = st.selectbox("Biggest pain point", PAIN_POINTS)
        submitted = st.form_submit_button("Generate 90-day playbook →", use_container_width=True, type="primary")

    if submitted:
        with st.spinner("Generating your playbook… (15–20 seconds)"):
            playbook = generate_playbook(org, industry, maturity, pain)
        if playbook:
            st.success("Playbook generated.")
            render_playbook(playbook)
            st.download_button(
                "⬇️ Download playbook (JSON)",
                data=json.dumps(playbook, indent=2),
                file_name="governance-playbook.json",
                mime="application/json",
            )


if __name__ == "__main__":
    main()
