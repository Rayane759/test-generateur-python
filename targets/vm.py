"""
Cible : VM on-premise — non implémentée (prévu pour une prochaine itération).
"""

from pathlib import Path


def generate_vm(values: dict, output_dir: Path) -> None:
    raise NotImplementedError(
        "La cible 'vm' n'est pas encore implémentée. "
        "Cibles disponibles : kubernetes"
    )