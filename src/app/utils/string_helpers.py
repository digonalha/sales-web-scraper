def str_to_float(text: str) -> float:
    cleaned_str = "".join(filter(str.isdigit, text))

    if len(cleaned_str) > 1:
        cleaned_str = cleaned_str[:-2] + "." + cleaned_str[-2:]
    else:
        cleaned_str = f"0.{cleaned_str}"
    

    return float(cleaned_str)
    
def sanitize_text(text: str) -> str:
    return None if not text else text.replace("\n", " ").strip()