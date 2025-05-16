import os
import pandas as pd

def is_complete(problem_name, programming_language, category):
    if programming_language == "python":
        ext = ".py"
    elif programming_language == "cpp":
        ext = ".cpp"
    else:
        raise Exception("Invalid Extension")

    problem_name = problem_name.lower().replace(" ", "_")
    problem_name = problem_name.replace("(", "").replace(")", "").replace("/", "") + ext
    
    if os.path.exists(os.path.join(programming_language, category, problem_name)):
        return "✔️"

    return "❌"

full_doc = "# Blind 75 Practice Problems"
df = pd.read_csv("problems.csv", usecols=["Category", "Name", "Difficulty", "Link"])

kw_map = {"Easy": 0, "Medium": 1, "Hard": 2}
# TODO incorporate programming language
for group, gdf in df.groupby("Category"):
    # Tables are grouped by Category, we do not need
    # to keep this column
    del gdf["Category"]

    # Sort df according to difficutly of problem
    gdf["Proxy"] = gdf.Difficulty.map(lambda x: kw_map[x])
    gdf = gdf.sort_values(by="Proxy")
    del gdf["Proxy"]

    # Check wheter Problem has been solved
    gdf[""] = gdf.Name.map(lambda x: is_complete(problem_name=x, programming_language="python", category=group))
    del gdf["Name"] # name is already stored in "Link", we dont need it twice
    
    # Check whether the problem has been completed
    table = gdf.to_markdown()

    # Document Describing problems solved under this domain
    curr_doc = f"\n## {group}\n\n{table}"
    
    with open(f"python/{group}/readme.md", "w") as f:
        f.write(curr_doc)
    
    group_link = group
    if " " in group_link:
        group_link = group.replace(" ", "%20")

    full_doc += f"\n- [{group}](python/{group_link})"

with open(f"./readme.md", "w") as f:
    f.write(full_doc)
