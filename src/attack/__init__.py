"""
Indirect Prompt Injection Attack Module.
Provides programmatic tools to generate, format, and embed indirect prompt injections
into retrieved documents across English, Hindi, Telugu, and Telugu-English Code-Mixed text.
"""

from src.attack.indirect_attack import IndirectAttackGenerator, AttackSample

__all__ = ["IndirectAttackGenerator", "AttackSample"]
