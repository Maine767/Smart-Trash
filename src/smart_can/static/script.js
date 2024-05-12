function send_data() {
    $.ajax({
        type: "GET",
        url: "/connect",
        dataType: "json",
        contentType: "application/json",
        data: {
            "sensor_id": document.getElementById("sensor_id").textContent,
            "amount": document.getElementById("amount").value,
        },
        
        success: function (response) {
            // Обновляем данные на странице после успешного запроса
            $('#status').text(response.status);
            $('#address').text(response.address);
            $('#percentage').text(response.percentage);
            $('#amount_of').text(response.amount_of);
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