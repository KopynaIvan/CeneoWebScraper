from deep_translator import Googletranslator
def extract_data(ancestor, selector, attribute=None, multiple=False):
    if selector:
        if multiple:
            if attribute:
                return [tag[attribute] for tag in ancestor.select(selector)]
            return [tag.get_text() for tag in ancestor.select(selector)]
        if attribute:
            try:
                return ancestor.select_one(selector)[attribute].strip()
            except TypeError:
                return None
        try:
            return ancestor.select_one(selector).get_text().strip()
        except AttributeError:
            return None
    try:
        return ancestor[attribute].strip()
    except (TypeError , KeyError):
        return None
def translate(text,source = "pl", target = "en"):
    return GoogleTranslator(source, target).translate(text=text)