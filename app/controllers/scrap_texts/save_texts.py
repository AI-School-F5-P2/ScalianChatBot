import os
from controllers.scrap_texts.clean_text import clean_text
from controllers.scrap_texts.clean_filename import clean_filename
from controllers.scrap_texts.advanced_filters import advanced_filters

def save_texts(title, text, url):
    """Save the title and text content to a file, with additional processing steps.
    Args:
        title (str): The title of the text.
        text (str): The content of the text.
        url (str): The URL associated with the text.
    Returns:
        None
    """
    is_url_filtered = True

    current_dir = os.path.dirname(__file__)
    texts_path = os.path.join(current_dir, "../..", "texts")
    spain_path = os.path.join(texts_path, "spain")
    global_path = os.path.join(texts_path, "global")

    clean_url = clean_filename(url)

    if not os.path.exists(texts_path):
        os.makedirs(texts_path)
        os.makedirs(spain_path)
        os.makedirs(global_path)

    file_path = os.path.join(
        spain_path if "scalian-spain" in url else global_path, f"{clean_url}.txt"
    )

    try:
        if "scalian-spain" in url or "scalian.com/es" in url:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text)
            clean_text(file_path)
            
            isActive = True
            advanced_filters(isActive, url, file_path)

            with open(file_path, "r+", encoding="utf-8") as f:
                content = f.read()
                f.seek(0)
                f.write(f"title: {title}\n")
                f.write(f"url: {url}\n\n")
                f.write(content)
            print(f"Texto escrito en texts/{clean_url}.txt\n")
    except Exception as e:
        print(f"Error al escribir texto: {e}")
