from typing import Dict, Any

def get_product_details(product_id: str) -> Dict[str, Any]:
    """Function form used by routers.products."""
    product_details = {
        "id": product_id,
        "name": "Sample Product",
        "description": "This is a sample product description.",
        "pairings": ["Product A", "Product B"],
        "suitable_for": ["Parties", "Everyday Use"],
        "image_url": "http://example.com/sample-product.jpg",
    }
    return product_details