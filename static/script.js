
function send_data() {
    $.ajax({
        type: "GET",
        url: "/connect",
        dataType: "json",
        contentType: "application/json",
        data: {
            "alert": document.getElementById("alert").value,
            "coordinates": document.getElementById("coordinates").value,
            "+1": document.getElementById("+1").value,
        },
        success: function (response) {
            console.log(response);
        }
    });
}
