
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
            console.log(response);
        }
    });
}
