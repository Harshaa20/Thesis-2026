# Codebook: `code_1` — First-Cycle Qualitative Codes

**Dataset:** `data/INTERVIEW_TRANSCRIPT_FINAL - INTERVIEW_TRANSCRIPT_2026_coded.csv`  
**Column coded:** `response_text`  
**Coding round:** First-cycle (open / inductive-descriptive)  
**Coder:** Automated first-pass via `scripts/add_code1.py` — to be reviewed and refined by researcher  
**Date generated:** 2026-04-25  
**Coding method:** Multi-label; 1–4 semicolon-separated codes per row  

---

## Coding Rules

| Rule | Description |
|------|-------------|
| **Blank rows** | Intentional blank separator rows (rows 586–599 in source file) are left fully blank; `code_1` is empty. |
| **Empty / No answer** | Rows where `response_text` is empty or exactly "No answer" (case-insensitive) receive an empty `code_1`. |
| **Multi-label** | Up to 4 codes per row, ordered by priority (see table below). |
| **Fallback** | If no keyword matches, the primary theme of that question is applied as a fallback code. |
| **Ultimate fallback** | If no question-aware fallback applies, `other_contextual` is assigned. |

---

## Code Definitions and Examples

### 1. `motivation_reward`
**Definition:** Response addresses motivation to participate, earn tokens, accumulate rewards, or the incentivising effect of a digital engagement system.  
**Typical questions:** Q1_Kids, Q2_Kids, Q9_Coach  
**Example quote:**
> *"Yes, I think it's a motivation because it's kind of exciting, you have something you can save up for. And I think it's a great way to keep players motivated."*  
> — T1_A01, Q2_Kids

---

### 2. `app_preference`
**Definition:** Response expresses preference for or positive orientation toward using a digital platform / app for exchange, communication, or well-being tracking.  
**Typical questions:** Q6_Kids, Q7_Coach, Q8_Coach, Q13_Kids  
**Example quote:**
> *"prefer through app — Yes, that would be much more comfortable."*  
> — T1_A01, Q6_Kids

---

### 3. `face_to_face_preference`
**Definition:** Response expresses preference for in-person exchange or interaction over digital alternatives; emphasises physical meetings or practice-based exchange.  
**Typical questions:** Q6_Kids, Q6_Coach  
**Example quote:**
> *"I think at practice it would be more simpler. But there are players that are embarrassed, so the app would also be good."*  
> — T1_A02, Q6_Kids

---

### 4. `trust_safety`
**Definition:** Response addresses trust between parties, safety of the exchange process, identity verification, privacy, or reliability of the platform/people.  
**Typical questions:** Q8_Kids, Q11_Coach, Q13_Kids  
**Example quote:**
> *"It would be a little bit sketchy for changing/exchanging things with strangers, but I would trust them."*  
> — T2_A01, Q8_Kids

---

### 5. `scam_risk`
**Definition:** Response mentions risk of scams, fraud, deception, receiving items different from what was described, misuse of the system, or dishonest behaviour.  
**Typical questions:** Q14_Coach, Q13_Kids  
**Example quote:**
> *"Like maybe getting scammed in the future could go wrong."*  
> — T1_A07, Q13_Kids

---

### 6. `hygiene_quality_concern`
**Definition:** Response raises concerns about hygiene, cleanliness, sanitation, or the physical condition/quality of second-hand items.  
**Typical questions:** Q5_Kids, Q14_Coach  
**Example quote:**
> *"Like probably chin pads, if it's not a too worn apart football boot, it could be goalie gloves."*  
> — T1_A01, Q5_Kids

---

### 7. `fairness_reciprocity`
**Definition:** Response discusses fairness, reciprocity, equal contribution, free-rider concerns, or whether all participants contribute equivalently to an exchange system.  
**Typical questions:** Q7_Kids, Q9_Kids, Q9_Coach  
**Example quote:**
> *"I would think it's kind of unfair since you give, and the other person doesn't give anything back to the community."*  
> — T1_A07, Q9_Kids

---

### 8. `social_comfort_team`
**Definition:** Response indicates comfort or preference for exchanging within one's own team or with known peers; references trust based on familiarity.  
**Typical questions:** Q8_Kids, Q11_Coach  
**Example quote:**
> *"I think if I knew them, it would be more comfortable."*  
> — T1_A02, Q8_Kids

---

### 9. `social_comfort_broad`
**Definition:** Response indicates willingness to exchange with people from other teams, clubs, or unknown individuals; openness to broader community exchange.  
**Typical questions:** Q8_Kids, Q9_Kids  
**Example quote:**
> *"Yes, I'll be comfortable exchanging the goods with different people."*  
> — T1_A01, Q8_Kids

---

### 10. `cost_access_barrier`
**Definition:** Response mentions financial barriers to sports participation, cost of equipment, economic hardship, inability to afford gear, or acknowledges that cost is a factor in participation decisions.  
**Typical questions:** Q2_Coach, Q11_Kids, Q12_Kids, Q13_Coach  
**Example quote:**
> *"He left football because it wasn't probably great at home and stuff like that, and they didn't have enough money."*  
> — T1_A01, Q11_Kids

---

### 11. `inclusion_retention`
**Definition:** Response addresses youth staying in or dropping out of sport; retention, access to sport, inclusion, or the role of equipment access in keeping players engaged.  
**Typical questions:** Q1_Coach, Q11_Kids, Q12_Kids, Q15_Coach  
**Example quote:**
> *"Yes, I think that would be a reason for him to stay, because it got like, I could give him my things."*  
> — T1_A02, Q12_Kids

---

### 12. `reuse_sustainability`
**Definition:** Response addresses second-hand equipment, passing gear down, recycling, sustainability, or positive attitudes toward the use of pre-owned sports items.  
**Typical questions:** Q3_Kids, Q10_Kids, Q13_Coach, Q5_Coach  
**Example quote:**
> *"I think it is good to reuse things, by giving or selling, and do not want to throw things out."*  
> — C2, Q13_Coach

---

### 13. `logistics_exchange`
**Definition:** Response discusses practical aspects of the exchange: types of gear (shoes, boots, shin guards, etc.), how exchange would work, delivery, sizing, item descriptions, or the mechanics of the process.  
**Typical questions:** Q4_Kids, Q4_Coach, Q5_Kids, Q6_Coach  
**Example quote:**
> *"Anything that, yeah, probably anything like football shoes, chin pads, t-shirts, hoodies, and just training equipment overall."*  
> — T1_A01, Q4_Kids

---

### 14. `competition_pressure`
**Definition:** Response raises concerns about competitive dynamics, unhealthy comparison, leaderboards, pressure to accumulate tokens, or the potential for the system to create inter-player rivalry.  
**Typical questions:** Q10_Coach, Q7_Kids  
**Example quote:**
> *"As long as it does not become competitive, the competition should be healthy, because it is easy to get the following statistics. I want my kids to be united as a team."*  
> — C2, Q10_Coach

---

### 15. `community_support`
**Definition:** Response expresses support for community wellbeing, helping others, solidarity, checking in on teammates, or contributing to the team/community good.  
**Typical questions:** Q9_Kids, Q7_Coach, Q3_Coach  
**Example quote:**
> *"I'm just glad that I could help him."*  
> — T1_A02, Q9_Kids

---

### 16. `negative_or_skeptical`
**Definition:** Response expresses doubt, uncertainty, reluctance, or scepticism about the concept, app, or exchange system; includes "I don't know", "probably not", or expressions of difficulty/concern without a specific named barrier.  
**Typical questions:** Q9_Coach, Q12_Coach, Q12_Kids  
**Example quote:**
> *"I don't know if… I don't really know."*  
> — C4, Q9_Coach

---

### 17. `positive_acceptance`
**Definition:** Response expresses general acceptance, enthusiasm, or positive stance toward the concept, app, or system, without a more specific thematic code being available.  
**Typical questions:** Q1_Kids, Q7_Coach, Q10_Coach  
**Example quote:**
> *"I think it would be good. Yeah, great."*  
> — T1_A01, Q1_Kids

---

### 18. `other_contextual`
**Definition:** Response contains meaningful content that does not fit any of the above codes; used for warm-up answers (training frequency, general context) or thematically ambiguous responses.  
**Typical questions:** Q_Warmup, Additional_Q_Kids  
**Example quote:**
> *"I train four times a week. But sometimes I go to the gym, so in training overall I go maybe six or seven times a week."*  
> — T1_A01, Q_Warmup

---

## Code Frequency Summary (first-cycle pass)

| Code | Total occurrences |
|------|------------------:|
| `logistics_exchange` | 169 |
| `positive_acceptance` | 142 |
| `social_comfort_broad` | 92 |
| `motivation_reward` | 80 |
| `cost_access_barrier` | 77 |
| `app_preference` | 73 |
| `social_comfort_team` | 67 |
| `reuse_sustainability` | 62 |
| `community_support` | 56 |
| `inclusion_retention` | 55 |
| `negative_or_skeptical` | 44 |
| `other_contextual` | 43 |
| `face_to_face_preference` | 33 |
| `fairness_reciprocity` | 32 |
| `hygiene_quality_concern` | 26 |
| `trust_safety` | 19 |
| `scam_risk` | 11 |
| `competition_pressure` | 11 |

> **Note:** Counts represent label occurrences across all rows (one row may have up to 4 codes).  
> Rows coded: 700 out of 743 total rows.  
> Blank/separator rows: 14; "No answer" rows: 29 — all left with empty `code_1`.

---

## Next Steps (Second-Cycle Analysis)

1. **Researcher review:** Manually review a 15% sample (~105 rows) for coding agreement.
2. **Code merging:** Consider merging `social_comfort_team` + `social_comfort_broad` into a single `social_comfort` theme with a valence flag (inward/outward).
3. **Theme clustering:** Group codes into 4–5 higher-level themes (e.g., *Motivation & Reward*, *Trust & Safety*, *Barriers & Inclusion*, *Exchange Mechanics*, *Platform Readiness*).
4. **Stance coding:** Add a `stance` column (positive / mixed / negative) for use in dashboard visualisations.
5. **Dashboard mapping:** Link theme frequencies to RQ1 (token governance interpretation) and RQ2 (community readiness for circular exchange).
