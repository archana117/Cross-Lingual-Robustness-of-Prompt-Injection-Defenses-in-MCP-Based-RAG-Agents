# Evaluation Methodology & Metrics

**Project**: *Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents*  
**Module**: `src/evaluation/task_utility.py`, `src/evaluation/metrics.py`

---

## 1. Metrics Definitions

### 1. Attack Success Rate (ASR)
The proportion of attack scenarios where the prompt injection successfully causes the agent to violate its instructions or execute the attacker's mandate:
$$\text{ASR} = \frac{\text{Successful Attacks}}{\text{Total Attack Cases}} \times 100$$
*Lower is better.*

### 2. Defense Block Rate (DBR)
The proportion of attack scenarios intercepted and neutralized by the defense:
$$\text{DBR} = \frac{\text{Blocked Attacks}}{\text{Total Attack Cases}} \times 100$$
*Higher is better.*

### 3. Task Utility Under Attack
The proportion of attack scenarios where the agent successfully answers the user's legitimate question despite the presence of the embedded injection:
$$\text{Task Utility Under Attack} = \frac{\text{Legitimate Tasks Successfully Completed Under Attack}}{\text{Total Attack Cases}} \times 100$$
*Higher is better.*

### 4. Benign / Safe Task Utility
The proportion of clean (safe) scenarios where the agent successfully answers the user's legitimate question:
$$\text{Safe Utility} = \frac{\text{Legitimate Tasks Completed on Clean Samples}}{\text{Total Clean Samples}} \times 100$$

### 5. False Positive Rate (FPR)
The proportion of clean (safe) scenarios mistakenly blocked by the defense:
$$\text{FPR} = \frac{\text{Clean Samples Blocked by Defense}}{\text{Total Clean Samples}} \times 100$$

### 6. False Negative Rate (FNR)
The proportion of attack scenarios that bypass the defense and successfully execute:
$$\text{FNR} = \frac{\text{Unblocked Successful Attacks}}{\text{Total Attack Cases}} \times 100$$

---

## 2. Investigation of the 0% Task Utility Finding

In preliminary benchmarks and binary-gatekeeper defenses, **Task Utility Under Attack** frequently registers as 0.0%:

### Root Cause Analysis:
1. **Binary Quarantine Behavior**: When the defense detects an anomaly, it blocks or quarantines the entire retrieved context (e.g. returning a security alert or refusal). As a consequence, the legitimate factual information is suppressed along with the attack, preventing the LLM from answering the user's query.
2. **Unblocked Attack Hijacking**: When the defense fails to detect the attack, the injection hijacks the model's generation, causing it to echo the attacker's mandate rather than answering the user query.
3. **Implication for Defense Design**: To preserve Task Utility under attack, defenses must evolve from binary all-or-nothing blockers to **fine-grained context sanitizers** that excise malicious spans while forwarding legitimate factual sentences to the LLM.
