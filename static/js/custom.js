

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

function sendArticleComment(articleId){
    event.preventDefault();
    var comment = $('#commentText').val();
    var parentId = $('#parentId').val() || null;
    console.log("Parent ID:", parentId);
    $.post('/post/article/add-article-comment/',{
     articleComment : comment ,
     articleID : articleId,
     parentId : parentId,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

    }).then(res=>{
        console.log("Response:", res);
        $('#comment_list').html(res);
        $('#commentText').val('');
        $('#parentId').val('');




        if (parentId !== null && parentId !==''){
            let newcomment=document.getElementById('single_comment_box_' + parentId);
            if (newComment) {
                newComment.scrollIntoView({ behavior: 'smooth' });
            }
            // scrollIntoView({behavior:'smooth'})
        }
        else {
            let lastComment=document.querySelector("#comment_list > div:last-child");
             if (lastComment) {
                lastComment.scrollIntoView({ behavior: 'smooth' });
            }
            // scrollIntoView({behavior:'smooth'})

        }
        })
    .fail(function(err) {
        console.error("Error:", err);
    });
}


function fillParentId(parentId){
    $('#parentId').val(parentId);
    document.getElementById('commentForm').scrollIntoView({behavior:"smooth"})
}




document.addEventListener("DOMContentLoaded", function () {
        let brandCheckboxes = document.querySelectorAll(".brand-filter");

        brandCheckboxes.forEach(checkbox => {
            checkbox.addEventListener("change", function () {
                let selectedBrands = [];
                document.querySelectorAll(".brand-filter:checked").forEach(cb => {
                    selectedBrands.push(cb.value);
                });

                let url = new URL(window.location.href);
                url.searchParams.delete("brands");
                selectedBrands.forEach(brand => url.searchParams.append("brands", brand));

                fetch(url, {
                    headers: { "X-Requested-With": "XMLHttpRequest" }
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById("product-list-container").innerHTML = data.html;
                });
            });
        });
    });