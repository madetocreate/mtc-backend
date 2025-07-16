def warn_if_too_long(text):
    if len(text.split()) > 2000:
        print("⚠️ Token-Limit überschritten!")
