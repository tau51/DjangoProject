var $editbtn = $("#btn_edit");
    $(function () {
        $editbtn.click(function () {
            var rows = $("#table").bootstrapTable('getSelections');
            alert(JSON.stringify(rows));
            if (rows.length === 2 || rows.length === 0 ) {
                alert("请选择单个数据编辑修改!");
                }
            else {
                $("#modal_club").val(rows[0].club);
                $("#modal_wechat").val(rows[0].wechat);
                $("#modal_note").val(rows[0].note);
                $("#myModal").modal();
            }

        });
    });
    $("#btn_add").click(function () {
        $("#myModalLabel").text("新增");
        $('#myModal').modal();
});