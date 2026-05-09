# Product Spec: Data Governance Playbook Generator
**Version:** 1.0  
**Status:** Draft  
**Author:** Vijay (xvor)  
**Last updated:** May 2026

---

## Problem statement

Enterprise data governance programmes have a high failure rate — not because organisations don't understand that governance matters, but because the path from "we need to govern our data" to "governance is operationalised and working" is poorly defined.

The two leading frameworks — DCAM (EDM Council) and DAMA DMBOK2 — are comprehensive but prescriptive. They describe *what* good looks like at full maturity. They don't answer the question practitioners actually face: **"Given where we are today, what should we do first?"**

The result: governance programmes that start with the wrong actions, lose stakeholder confidence early, and stall before they deliver value. Or worse — they produce governance theatre: policies, councils, and catalogues that nobody uses.

---

## Who this is for

### Primary persona — The Data Office Programme Lead
**Who:** A senior data governance practitioner, newly appointed Data Office Leader, or CDO direct report who has been tasked with "standing up data governance" or "maturing our data capability."  
**Context:** Has framework knowledge (or is rapidly acquiring it), understands the organisational politics, and needs to produce a credible 90-day plan — fast.  
**Pain:** Every governance framework gives them a destination, not a starting point. Generic playbooks from consultants don't account for their industry, their maturity level, or their specific pain.  
**What they need:** A starting point that is specific enough to be defensible in front of a CDO or executive sponsor, grounded in recognised frameworks, and fast to produce.

### Secondary persona — The CDO or VP of Data
**Who:** Sponsors the governance programme. Doesn't run it day-to-day but needs confidence that the approach is sound.  
**Context:** Has seen governance programmes fail. Sceptical of generic consulting decks.  
**Pain:** Hard to evaluate whether a proposed governance plan is appropriately sequenced and grounded in recognised practice.  
**What they need:** A plan they can interrogate — with explicit framework references, clear success signals, and realistic phasing.

### Out of scope (V1)
- Data engineers or analysts looking for technical data quality tools
- Organisations seeking regulatory compliance checklists (GDPR, HIPAA) — this is governance capability, not compliance documentation
- Consultancies looking to white-label a client deliverable tool

---

## What it does (V1 scope)

A web application that takes four structured inputs and generates a tailored 90-day data governance playbook.

**Inputs:**
| Input | Options | Why it matters |
|---|---|---|
| Organisation type | Large enterprise, mid-size, scale-up, public sector | Determines operating model complexity and change velocity |
| Industry | 7 industries including financial services, industrial/energy, healthcare, technology | Determines regulatory context, data domain specifics, and common failure modes |
| DCAM maturity level | 5 levels from Not Initiated to Optimising | Single most important variable — wrong-level advice is worse than no advice |
| Biggest pain point | 6 options covering quality, compliance, ownership, AI readiness, silos, metadata | Anchors Phase 1 to the problem that has executive attention right now |

**Output:** A structured 90-day playbook with:
- 3 phases of 30 days, each with a theme and objective
- 3 actions per phase — specific, verb-led, industry-aware
- DCAM component tag per action
- DMBOK knowledge area tag per action
- Success signal (observable definition of done)
- Effort level and key stakeholders

**Download:** Full playbook exportable as JSON for use in project management tools or internal documentation.

---

## What it does not do (explicit V1 exclusions)

These are deliberate scope decisions, not oversights:

| Excluded | Reason |
|---|---|
| Execution tracking / check-ins | V2 feature — requires persistence layer and changes the UX model significantly |
| Regulatory compliance mapping (GDPR, DPDP, EU AI Act) | Out of scope for governance capability tool; separate product surface |
| Team collaboration / multi-user | V2 — adds auth and sharing complexity without validating core value first |
| Pre-built playbook templates | Defeats the purpose — specificity is the core value proposition |
| Integration with data catalogue tools | V2 — high integration cost, validates after core adoption |

---

## Success metrics

### V1 launch (0–90 days)
| Metric | Target | Notes |
|---|---|---|
| Playbooks generated | 200 | Proxy for tool discovery and basic utility |
| JSON downloads | 30% of generations | Signals intent to actually use the output |
| Return visits | 20% of users | Signals the tool produced something worth coming back to |
| GitHub stars | 50 | Proxy for practitioner credibility |

### V1 validation questions (qualitative)
- Do practitioners find the DCAM maturity differentiation meaningful, or do outputs feel generic across levels?
- Is the 90-day structure the right frame, or do users want shorter sprints or longer horizons?
- Who is actually using this — governance practitioners, consultants, or students learning the frameworks?

---

## V1 vs V2 scope decisions

### Why execution tracking is V2, not V1
The Playbook Scorecard — 30/60/90 check-ins, DCAM gap re-scoring, adaptive Phase 2/3 regeneration — is the feature that transforms this from a generator into a product. It requires:
- Persistent storage (currently file-based, needs proper backend at scale)
- A return UX model (users need a reason and reminder to come back)
- Validation that users actually execute the playbooks they generate (unproven in V1)

Shipping it in V1 would add significant complexity before validating that the core generation is useful. The right sequencing: validate generation utility first, then add tracking.

### Why the PRD itself is a V1 deliverable
Most open-source governance tools ship without any product thinking documentation. Including a product spec in the repo signals that this was designed, not just coded — and gives practitioners a model for how to think about deploying governance tooling inside their own organisations.

---

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Generated playbooks are too generic despite inputs | Medium | High — kills core value prop | Continuous prompt refinement; maturity level descriptions in prompt are the key lever |
| DCAM/DMBOK framework knowledge becomes stale | Low | Medium | Framework versions are stable; DCAM 3.0 and DMBOK2 are current standards |
| Users generate but don't act — "governance theatre" risk | High | Low for tool (high for org) | V2 scorecard directly addresses this; V1 README acknowledges it explicitly |
| LLM output quality variance | Medium | Medium | JSON schema enforcement in prompt; error handling with retry |

---

## Open questions for V2 scoping

1. **Persistence model** — file-based JSON works for single-user local deployment. What's the right persistence model for a hosted version? (Supabase, Firebase, or stay file-based with export?)
2. **Scorecard trigger** — how does a user know when to do their 30-day check-in? Email reminder, in-app nudge, or purely manual?
3. **Adaptive regeneration** — if Phase 1 is 40% complete, does V2 regenerate Phase 2 entirely, or amend it? Regeneration risks losing user context; amendment requires diff logic.
4. **Collaborative mode** — Data Office programmes involve multiple people. Is a single-user tool the right model, or does V2 need a team view?

---

## Appendix: Framework reference

See `framework_reference.py` for full DCAM component descriptions, DMBOK knowledge area definitions, and the DCAM→DMBOK cross-mapping used by the playbook generator.

---

*This spec is part of the `data-governance-playbook-generator` open-source project by [xvor](https://github.com/xvor).*
