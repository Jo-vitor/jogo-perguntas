"""Legacy game module kept for compatibility.

The new runtime entrypoint has moved to :mod:`src.engine`.
"""

from src.engine import executar_jogo


__all__ = ["executar_jogo"]
