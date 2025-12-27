import pathway as pw
import os

def start_pathway_pipeline(data_path="./data"):
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    # Pathway streams the files. If a file changes, the table updates automatically.
    raw_data = pw.io.fs.read(
        data_path,
        format="plaintext",
        mode="streaming",
        with_metadata=True
    )
    
    return raw_data