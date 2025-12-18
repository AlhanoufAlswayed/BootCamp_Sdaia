from __future__ import annotations
from pathlib import Path
import json


def render_json(report: dict) -> str:
    return json.dumps(report, indent=2, ensure_ascii=False) + "\n"


def render_markdown(report: dict) -> str:
    lines: list[str] = []
    lines.append("# CSV Report\n")
    lines.append(f"Rows: {report.get('rows', 0)}\n")
    for col, info in report.get("columns", {}).items():
        line = f"- {col}: {info.get('type')} , missing: {info.get('missing')}"
        if info.get("type") == "number":
            line += (
                f" , count: {info.get('count')} , unique: {info.get('unique')}"
                f" , min: {info.get('min'):.2f} , max: {info.get('max'):.2f} , mean: {info.get('mean'):.2f}"
            )
        elif info.get("type") == "text" and "top" in info:
            top_vals = ", ".join(
                f'{t["value"]} ({t["count"]})' for t in info["top"])
            line += f" , top: {top_vals}"
        lines.append(line)

    return "\n".join(lines) + "\n"


def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_json(report))


def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(report))