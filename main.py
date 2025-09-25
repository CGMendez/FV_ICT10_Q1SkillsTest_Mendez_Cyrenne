from pyscript import document

def order_form(e):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value
    quantity = document.getElementById("quantity").value

    message = f"""
    <div class = 'result'> Order for:</div>
    Name: {name} <br>
    Address: {address} <br>
    Contact: {contact} <br>
    Quantity: {quantity} <br>


    <br>
    <span class = 'result'>Thank you for Ordering with us!</span>
        """
    
    result = document.getElementById("result")
    result.innerHTML = message
    result.style.display = "block"

