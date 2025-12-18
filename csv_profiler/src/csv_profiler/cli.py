import typer
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import write_json, write_markdown

app = typer.Typer()


@app.command()
def greeting_user(name: str):
    print(f"Hello {name}, welcome to the CSV Profiler!")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Mr. {name}, it was a pleasure assisting you.")
    else:
        print(f"See you later, {name}!")


@app.command()
def profile_csv(input_file: str, json_output: str, md_output: str):
    rows = read_csv_rows(input_file)
    report = basic_profile(rows)
    write_json(report, json_output)
    write_markdown(report, md_output)
    print(f"Wrote {json_output} and {md_output}")


if __name__ == "__main__":
    app()