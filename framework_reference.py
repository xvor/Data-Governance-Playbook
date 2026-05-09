"""
framework_reference.py
Standalone reference module for DCAM and DAMA-DMBOK2 frameworks.
Useful for understanding the concepts behind the playbook generator.
Run: python framework_reference.py
"""

DCAM_OVERVIEW = {
    "full_name": "Data Management Capability Assessment Model",
    "owner": "EDM Council",
    "purpose": "Assess and improve an organisation's data management capabilities across 8 components",
    "maturity_levels": {
        1: ("Not Initiated", "No formal capability exists"),
        2: ("Conceptual", "Awareness exists but nothing formalised"),
        3: ("Developmental", "Work underway but inconsistent"),
        4: ("Defined", "Formalised and consistently applied"),
        5: ("Optimising", "Measured and continuously improved"),
    },
    "components": {
        "Data Management Strategy": {
            "description": "Defines the vision, objectives, and roadmap for data as a strategic asset",
            "key_outputs": ["Data strategy document", "Roadmap", "KPIs for data value"],
            "typical_pain_addressed": "No shared vision for data across the org",
        },
        "Data Management Business Case": {
            "description": "Justifies investments in data management with quantified business value",
            "key_outputs": ["Cost-benefit analysis", "ROI model", "Risk quantification"],
            "typical_pain_addressed": "Leadership won't fund governance programs",
        },
        "Data Management Program and Funding": {
            "description": "Establishes the operating model, team structure, and budget for data management",
            "key_outputs": ["Org chart", "Budget allocation", "Operating model"],
            "typical_pain_addressed": "No dedicated team or budget for data",
        },
        "Data Governance": {
            "description": "Defines policies, roles (Data Owners, Stewards, Custodians), and decision rights",
            "key_outputs": ["Data policy", "RACI matrix", "Data council charter"],
            "typical_pain_addressed": "Unclear ownership and accountability",
        },
        "Data Architecture": {
            "description": "Designs the logical and physical structure of data assets and flows",
            "key_outputs": ["Data architecture diagram", "Canonical data model", "Integration patterns"],
            "typical_pain_addressed": "Data silos and inconsistent data models",
        },
        "Data Quality Management": {
            "description": "Defines and enforces standards for data accuracy, completeness, and timeliness",
            "key_outputs": ["DQ rules", "DQ scorecard", "Remediation workflows"],
            "typical_pain_addressed": "Teams don't trust the data",
        },
        "Data Management Operations Risk and Control": {
            "description": "Manages operational risk, compliance, security, and audit requirements for data",
            "key_outputs": ["Risk register", "Control catalogue", "Audit trails"],
            "typical_pain_addressed": "Regulatory non-compliance and audit failures",
        },
        "Analytics Management": {
            "description": "Governs the use of data for analytics, BI, and AI/ML applications",
            "key_outputs": ["Analytics governance policy", "Model registry", "Use case evaluation framework"],
            "typical_pain_addressed": "AI/ML projects fail due to poor data foundations",
        },
    },
}

DMBOK_OVERVIEW = {
    "full_name": "Data Management Body of Knowledge",
    "edition": "2nd Edition (DMBOK2)",
    "owner": "DAMA International",
    "purpose": "Comprehensive guide to data management practice across 10 knowledge areas",
    "knowledge_areas": {
        "Data Governance": {
            "description": "Planning, oversight, and control over data management and use",
            "key_practices": ["Establishing data councils", "Defining policies", "Assigning stewardship"],
        },
        "Data Architecture": {
            "description": "Defining the blueprint for managing data assets aligned to business strategy",
            "key_practices": ["Enterprise data model", "Data flow diagrams", "Technology architecture"],
        },
        "Data Modeling and Design": {
            "description": "Discovering, analysing, and representing data requirements",
            "key_practices": ["Conceptual / logical / physical models", "Entity-relationship diagrams"],
        },
        "Data Storage and Operations": {
            "description": "Designing, implementing, and managing data stores",
            "key_practices": ["Database administration", "Data retention", "Backup and recovery"],
        },
        "Data Security": {
            "description": "Ensuring privacy, confidentiality, and appropriate access to data",
            "key_practices": ["Access control", "Data classification", "Masking and encryption"],
        },
        "Data Integration and Interoperability": {
            "description": "Acquiring, processing, and moving data between systems",
            "key_practices": ["ETL/ELT pipelines", "API design", "Master data integration"],
        },
        "Reference and Master Data": {
            "description": "Managing shared data to reduce redundancy and ensure consistency",
            "key_practices": ["Golden record creation", "MDM platform", "Reference data registry"],
        },
        "Data Warehousing and Business Intelligence": {
            "description": "Enabling reporting and analysis to support decision-making",
            "key_practices": ["Data warehouse design", "BI tool governance", "Self-service analytics"],
        },
        "Metadata Management": {
            "description": "Collecting, organising, and making accessible data about data",
            "key_practices": ["Data catalogue", "Business glossary", "Data lineage"],
        },
        "Data Quality": {
            "description": "Defining, monitoring, and improving data quality dimensions",
            "key_practices": ["Profiling", "Quality rules", "DQ dashboards", "Remediation workflows"],
        },
    },
}

DCAM_DMBOK_MAPPING = {
    "Data Management Strategy":               ["Data Governance", "Data Architecture"],
    "Data Management Business Case":          ["Data Governance"],
    "Data Management Program and Funding":    ["Data Governance"],
    "Data Governance":                        ["Data Governance", "Reference and Master Data"],
    "Data Architecture":                      ["Data Architecture", "Data Modeling and Design", "Data Integration and Interoperability"],
    "Data Quality Management":                ["Data Quality", "Metadata Management"],
    "Data Management Operations Risk and Control": ["Data Security", "Data Storage and Operations"],
    "Analytics Management":                   ["Data Warehousing and Business Intelligence", "Metadata Management"],
}


def print_dcam_summary() -> None:
    print("=" * 60)
    print("DCAM — Data Management Capability Assessment Model")
    print("EDM Council | edmcouncil.org/frameworks/dcam/")
    print("=" * 60)
    print("\nMATURITY LEVELS:")
    for level, (name, desc) in DCAM_OVERVIEW["maturity_levels"].items():
        print(f"  Level {level} — {name}: {desc}")
    print("\nCOMPONENTS:")
    for comp, detail in DCAM_OVERVIEW["components"].items():
        print(f"\n  {comp}")
        print(f"    {detail['description']}")
        print(f"    Pain addressed: {detail['typical_pain_addressed']}")


def print_dmbok_summary() -> None:
    print("\n" + "=" * 60)
    print("DAMA DMBOK2 — Data Management Body of Knowledge")
    print("DAMA International | dama.org")
    print("=" * 60)
    print("\nKNOWLEDGE AREAS:")
    for area, detail in DMBOK_OVERVIEW["knowledge_areas"].items():
        print(f"\n  {area}")
        print(f"    {detail['description']}")


def print_mapping() -> None:
    print("\n" + "=" * 60)
    print("DCAM → DMBOK MAPPING")
    print("=" * 60)
    for dcam, dmbok_list in DCAM_DMBOK_MAPPING.items():
        print(f"\n  {dcam}")
        for d in dmbok_list:
            print(f"    → {d}")


if __name__ == "__main__":
    print_dcam_summary()
    print_dmbok_summary()
    print_mapping()
    print("\n")
