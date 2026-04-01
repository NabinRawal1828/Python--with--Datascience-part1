import json
import os

# List of notebooks to merge
notebooks = [
    "Demo.ipynb",
    "Operators.ipynb",
    "Built _in _Functions.ipynb",
    "Control-flow-statement.ipynb",
    "Looping statement.ipynb",
    "Interview-Questions.ipynb",
    "Question.ipynb"
]

merged_cells = []

# Read all notebooks and merge their cells
for notebook_file in notebooks:
    file_path = os.path.join(".", notebook_file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
            # Add section header
            merged_cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# {notebook_file.replace('.ipynb', '')}\n"],
                "id": f"section-{notebook_file}"
            })
            # Add all cells from this notebook
            merged_cells.extend(notebook.get('cells', []))
    except Exception as e:
        print(f"Error reading {notebook_file}: {e}")

# Create merged notebook structure
merged_notebook = {
    "cells": merged_cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.10.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

# Save merged notebook
output_file = "Python-Complete-Guide.ipynb"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_notebook, f, indent=1, ensure_ascii=False)

print(f"✅ Merged notebook created: {output_file}")
print(f"Total cells: {len(merged_cells)}")
