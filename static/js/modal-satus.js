$(documento).ready(function()
{
    $('#modal-status').ready(function(){
        var status = $('input:hidden[name=modal-status]').valueOf();
        if(status== 'show'){
            var myModal= new bootstrap.Modal(document.getElementById('maiModal'));
            myModal.show();
            }
    });

});

