function send_data() {
    $.ajax({
        type: "GET",
        url: "/connect",
        dataType: "json",
        contentType: "application/json",
        data: {
            "sensor_id": document.getElementById("sensor_id").textContent,
            "add": document.getElementById("add").value,
            "status": document.getElementById("status").textContent,
            "address": document.getElementById("address").textContent,
            "amount": document.getElementById("amount").textContent,

        },
        
        success: function (response) {
            // Обновляем данные на странице после успешного запроса
            $('#status').text(response.status);
            $('#address').text(response.address);
            $('#percentage').text(response.percentage);
            $('#amount').text(response.amount);
            console.log(response);
        }
    });
}


document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("myForm").addEventListener("submit", function(event) {
        event.preventDefault();
        var sensor_id = document.getElementById("sensor_id").value;

        window.location.href = "http://127.0.0.1:5000/settings/sensor/" + sensor_id;
    });
});