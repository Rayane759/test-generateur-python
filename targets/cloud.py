"""
Cible : Cloud (AWS / GCP / Azure) — non implémentée (prévu pour une prochaine itération).
"""

from pathlib import Path


def generate_cloud(values: dict, output_dir: Path) -> None:
    raise NotImplementedError(
        "La cible 'cloud' n'est pas encore implémentée. "
        "Cibles disponibles : kubernetes"
    )