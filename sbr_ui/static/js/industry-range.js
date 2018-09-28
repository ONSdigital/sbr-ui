$(function () {
    $("#showPasswordToggle").click(function () {
        if ($(this).is(":checked")) {
            $("#range").show();
            $("#single").hide();
        } else {
            $("#single").show();
            $("#range").hide();
        }
    });
});
