from csv_profiler.helper import is_missing, infer_type, numeric_stats, text_stats


def basic_profile(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"rows": 0, "columns": {}}

    col_names = list(rows[0].keys())
    columns = {}

    for col in col_names:
        values = [row.get(col, "") for row in rows]
        col_type = infer_type(values)

        if col_type == "number":
            stats = numeric_stats(values)
        else:
            stats = text_stats(values)

        col_info = {"type": col_type, **stats}
        columns[col] = col_info

    return {
        "rows": len(rows),
        "columns": columns
    }