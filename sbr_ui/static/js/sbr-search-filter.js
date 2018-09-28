$(function () {
    $("#showPasswordToggle").click(function () {
        if ($(this).is(":checked")) {
            $("#enterprise").hide();
            $("#local-unit-one").hide();
            $("#ch-unit-one").hide();
        } else {
          $("#enterprise").show();
          $("#local-unit-one").show();
          $("#ch-unit-one").show();
        }
    });
});
