import pandas as pd
import os

def is_complete(problem_name, dir_name):
    if dir_name == "python":
        ext = ".py"
    elif dir_name == "cpp":
        ext = ".cpp"
    else:
        raise Exception("Invalid Extension")

    problem_name = problem_name.lower().replace(" ", "_")
    problem_name = problem_name.replace("(", "").replace(")", "").replace("/", "")
    # print(problem_name)
    if os.path.exists(os.path.join(dir_name, problem_name + ext)):
        return "✔️"

    return "❌"

full_doc = "# Blind 75 Practice Problems"
df = pd.read_csv("problems.csv", usecols=["Category", "Name", "Difficulty", "Link"])

kw_map = {"Easy": 0, "Medium": 1, "Hard": 2}
for group, gdf in df.groupby("Category"):
    # Tables are grouped by Category, we do not need
    # to keep this column
    del gdf["Category"]

    # Sort df according to difficutly of problem
    gdf["Proxy"] = gdf.Difficulty.map(lambda x: kw_map[x])
    gdf = gdf.sort_values(by="Proxy")
    del gdf["Proxy"]

    # Check wheter Problem has been solved
    gdf[""] = gdf.Name.map(lambda x: is_complete(x, "python"))
    del gdf["Name"] # name is already stored in "Link", we dont need it twice
    
    # Check whether the problem has been completed
    table = gdf.to_markdown()
    full_doc += f"\n## {group}\n\n{table}"

with open("readme.md", "w") as f:
    f.write(full_doc)
