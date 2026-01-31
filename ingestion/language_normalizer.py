
def normalize(text: str) -> str:
    """
    Deployment-safe normalizer.
    Hindi translation is disabled in cloud deployment
    due to model and Python version limitations.
    """
    return text
