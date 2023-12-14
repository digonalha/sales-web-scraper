from src.app.dtos.sale_dto import SaleDto

def test_sale_dto_as_dict():
    # Arrange
    url = 'https://example.com'
    product_name = 'Example Product'
    product_price = 9.99
    description = 'This is an example product'

    sale = SaleDto(url=url, product_name=product_name, product_price=product_price, description=description)

    # Act
    result = sale.as_dict()

    # Assert
    assert result == {
        'url': url,
        'product_name': product_name,
        'product_price': str(product_price),
        'description': description
    }