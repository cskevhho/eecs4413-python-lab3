document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('cartForm').addEventListener('submit',
        function (event) {
            event.preventDefault();
            var noItems = parseInt(document.getElementById('no_items').value);
            var price = parseFloat(document.getElementById('price').value);
            var tax = parseFloat(document.getElementById('tax').value);
            if (noItems <= 0) {
                alert("Number of items must be a positive integer.");
                return;
            }
            if (price <= 0) {
                alert("Price must be a positive number.");
                return;
            }
            if (tax < 0 || tax > 100) {
                alert("Tax rate must be between 0 and 100.");
                return;
            }
            document.getElementById("cartForm").submit(); // needed this line for lab3 to work last time too
        });
});