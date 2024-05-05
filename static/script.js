
function send_data() {
    $.ajax({
        type: "GET",
        url: "/connect",
        dataType: "json",
        contentType: "application/json",
        data: {
            "id": document.getElementById("id").textContent,
            "amount": document.getElementById("amount").value,
        },
        
        success: function (response) {
            // Обновляем данные на странице после успешного запроса
            $('#status').text(response.status);
            $('#address').text(response.address);
            $('#percentage').text(response.percentage);
            $('#am_of').text(response.am_of);
            console.log(response);
        }
    });
}


document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("myForm").addEventListener("submit", function(event) {
        event.preventDefault();
        var selected_id = document.getElementById("sensor_id").value;

        window.location.href = "http://127.0.0.1:5000/" + selected_id;
    });
});