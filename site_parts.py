def test():
    return "this is from a function"

def slice():
    productCode = "1234-Sunglasses"
    productId = productCode[0:4]
    productId2 = productCode[:4]
    return f"""
    <p>product code: {productCode}</p>
    <p>product id: {productId}</p>
    <p>product id2: {productId2}</p>
    """

def header():
    return """
<html>
    <head>
        <title>Python</title>
        <style>
            body {
                font-family: monospace;
                background-color: #ccc;
            }
            h4 {
                background-color: #aaa;
            }
        </style>
    </head>
<body>
    """

