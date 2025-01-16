

function addProductToOrder(productID) {
    const ProductCount = $('#product_count').val();
    $.get('/order/add-to-order?product_id=' + productID + '&count=' + ProductCount).then(res => {
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button_text
        }).then( (result) =>{
            if(result.isConfirmed && res.status ==='not_logged_in'){
                window.location.href='/account/login'
            }
            }

        )
        ;


// if (res.status === 'success') {
//             Swal.fire({
//                 title: "اعلان",
//                 text: "محصول مورد نظر با موفقیت ثبت شد",
//                 icon: "success",
//                 showCancelButton: false,
//                 confirmButtonColor: "#3085d6",
//                 confirmButtonText: "باشه ممنون"
//             });
//         }

    });
}

function removeOrderDetail(detailId) {
    $.get('/dashboard/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}

function changeOrderDetailCount(detailId, state){
    $.get('/dashboard/change-order-detail?detail_id=' +detailId+'&state='+state).then(res=>{
        if (res.status === 'success'){
            $('#order-detail-content').html(res.body);
        }
    });
}


