# Defense Implementations Documentation

**Project**: *Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents*  
**Package**: `src/defenses/`

---

## 1. Defense Architecture Overview

All defenses conform to the standardized abstract contract `BaseDefense` (`src/defenses/base.py`):

```python
class BaseDefense(ABC):
    @abstractmethod
    def inspect(self, user_instruction: str, retrieved_context: str, reasoning_trace: Optional[str] = None) -> Dict[str, Any]:
        """Returns is_attack_detected, anomaly_score, action_taken ('ALLOW' | 'BLOCK'), and diagnostic details."""
```

---

## 2. Implemented Defense Conditions

### Condition A: No Defense (`NoDefense`)
- **Type**: Unmitigated baseline.
- **Mechanism**: Transparent pass-through.
- **Purpose**: Establishes the upper bound of vulnerability and records raw Attack Success Rate (ASR) when no security layer is active.

### Condition B: Prompt Filter / Perimeter (`PromptFilterDefense`)
- **Type**: Surface regex / keyword delimiter filter.
- **Mechanism**: Scans incoming context for known jailbreak tokens and override markers across English, Hindi, and Telugu.
- **Limitation**: Highly vulnerable to semantic paraphrasing, plain-text imperatives, and novel phrasing lacking explicit trigger words.

### Condition C: Meticulous Thought Defender (`ThoughtDefenderDefense`)
- **Type**: Semantic Chain-of-Thought (CoT) anomaly detector.
- **Mechanism**:
  1. Deconstructs the reasoning process into sequential steps.
  2. Embeds each step into 1,024-dimensional dense vectors using `BAAI/bge-m3`.
  3. Calculates pairwise consecutive cosine similarities $S(i, i+1)$ and path-level mean consistency.
  4. Calculates an anomaly score:
     $$\text{anomaly\_score} = 0.45 \cdot \text{deficit}_{\text{min}} + 0.45 \cdot \text{drop}_{\text{max}} + 0.10 \cdot \text{deficit}_{\text{path}}$$
  5. Flags the trace as `PROMPT_INJECTION` if the anomaly score exceeds threshold $\tau = 0.30$.
  6. Backtracks the suspicious step index using DFS tree traversal.

---

## 3. Cross-Lingual Semantic Distance Finding

Evaluation reveals that multilingual text (Hindi, Telugu, Telugu-English) exhibits wider natural semantic dispersion in `BGE-M3` vector space compared to controlled English step sequences. Consequently, static thresholds calibrated purely on English data experience elevated false positive rates in non-English contexts, indicating that adaptive per-language threshold calibration is required for multilingual RAG defense.
