import pathway as pw
import os
import io
import pypdf

# Global store to hold live data
# format: { internal_key: row_data_string }
latest_context = {}

@pw.udf
def parse_file_content(data: bytes, path: str) -> str:
    """
    Parses file content based on extension.
    Supports .pdf and plain text files.
    """
    import io
    import pypdf
    try:
        # Fix for Pathway Json object
        if not isinstance(path, str):
            path = str(path)
            # If it's a JSON string representation, it might have quotes.
            # But simple str() on a Json object might be sufficient or might need more.
            # If it looks like "foo.txt", strip check.
            if path.startswith('"') and path.endswith('"'):
                path = path[1:-1]
        
        if path.endswith(".pdf"):
            # Ensure data is bytes
            if not isinstance(data, bytes):
                return f"[Error: data is not bytes for {path}, type: {type(data)}]"
                
            reader = pypdf.PdfReader(io.BytesIO(data))
            text = []
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text.append(extracted)
            parsed = "\n".join(text)
            print(f"Parsed PDF {path}: {len(parsed)} chars")
            return parsed
        elif path.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Handle Images
            if not isinstance(data, bytes):
                 return f"[Error: data is not bytes for {path}, type: {type(data)}]"
            
            # Use local import to avoid circular dependency issues at top level if any
            from agent import get_image_description
            description = get_image_description(data)
            print(f"Parsed Image {path}: {len(description)} chars")
            return description
        else:
            # valid for .txt, .md, .csv etc.
            # Try/except for decoding
            try:
                decoded = data.decode("utf-8")
                return decoded
            except UnicodeDecodeError:
                 return f"[Error decoding {path}: Not UTF-8]"
    except Exception as e:
        print(f"Error parsing {path}: {e}")
        return f"[Error parsing {path}: {str(e)}]"

def update_context(key, row, time, is_addition):
    """
    Callback for Pathway's subscribe.
    Update the global latest_context dictionary based on changes.
    """
    global latest_context
    if is_addition:
        # row contains 'parsed_data' from our UDF
        if row and 'parsed_data' in row:
            latest_context[key] = row['parsed_data']
    else:
        # If is_addition is False, it's a deletion
        if key in latest_context:
            del latest_context[key]

def start_pathway_pipeline(data_path="./data"):
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    # Read as binary to handle PDFs
    files_table = pw.io.fs.read(
        data_path,
        format="binary",
        mode="streaming",
        with_metadata=True
    )
    
    # Apply the parsing UDF
    # pw.io.fs.read with with_metadata=True provides a '_metadata' column
    # Access path from _metadata
    parsed_table = files_table.select(
        parsed_data=parse_file_content(pw.this.data, pw.this._metadata["path"]),
        path=pw.this._metadata["path"]
    )

    # Subscribe to changes on the transformed table
    pw.io.subscribe(parsed_table, update_context)

    # We return the global store so the app can read from it
    return latest_context