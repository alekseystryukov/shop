$(document).ready(function(){
    var quantity_field = $('#id_quantity'),
        price_val = parseFloat($('#product_price').text()),
        sum_output = $('#purchase_sum');
    quantity_field.on('change', function(){
        var val = parseFloat(quantity_field.val());
        if(val > 0)
            sum_output.text(Math.round(val * price_val *100)/100);
    })
});