$(document).ready(function(){
  
  $('html,body').scrollTop(0);

              //common
   //수량카운트
   $('#remove').click(function(e){
    e.preventDefault();
    var stat=$('#number').text();
    var num=parseInt(stat,10);
    num --;
    if(num<=0){
      alert();
      num=1;
    }

    $('#number,.number').text(num);
    $('.wrap_price').text(num*15000);
  });

  $('#add').click(function(e){
    e.preventDefault();
    var stat=$('#number').text();
    var num=parseInt(stat,10);
    num ++;
    if(num>10){
      alert();
      num=10;
    }

    $('#number,.number').text(num); 
    $('.wrap_price').text(num*15000);
  });
  
   //click_baige
   var boxwrap=$('.click_e')
   $(boxwrap).focusin(function(){
       $(this).find('.box').addClass('baige')
       boxwrap.not($(this)).find('.box').removeClass('baige')
   })


              //e-common



   //menu

   $('.menu_bg').hide();
   $('.menu').click(function(){
     $('.menu_bg').fadeIn(300);
     $('.fix').animate({left:0},300)
     $('.fix').css({'opacity':'1','display':'block'})
     $('body').addClass('not_scroll')
   })

   $('.sub_menu1,.sub_menu2').hide()
   $('.get_sub1').click(function(){
 
     $('.sub_menu1').stop().slideToggle(500);
     
   })
   $('.get_sub2').click(function(){
     $('.sub_menu2').stop().slideToggle(400);
 
   })
   
   $('.exit,.menu_bg').click(function(){
     $('.menu_bg').fadeOut(300);
     $('.fix').animate({left:-330},300);
     $('.fix').css({'opacity':'0','display':'none'});
     $('.sub_menu1,.sub_menu2').hide();
     $('body').removeClass('not_scroll')

   })

   //about

  $(window).scroll(function(){
    var scrolltop = $(window).scrollTop();
    if(scrolltop>=0){
      $('.about_desc').css({'left':'10%%','opacity':0}).animate({'left':'0','opacity':1},1200);
    }
  })

  $(window).scroll(function(){
    var scrolltop = $(window).scrollTop();
    if(scrolltop>150){
      $('.brand_wrap').css({opacity:0}).animate({opacity:1},1200);
    }
  })

  //cart

  $('.empty_basket').hide()
  $('.del_btn').click(function(){
    $('.basket,.paysection,.cart_main').hide();
    $('.empty_basket').show()
    alert('삭제하시겠습니까?');
  })
  //howto
  $('.video_product').hide()
  $('.howto_video').click(function(){
    $(this).next().stop().slideToggle();
  })

  //login

  //회원가입

  //service_clean

  //srvice_wrap

  //payment
  $('.remove_selitem').click(function(){
    $(this).parents('.pickitem_wrap').hide()
  })
  //shop_all

  //shop_info

    //g_review,g_info

    $('.g_review').click(function(e){
      $(this).addClass('on')
      $('.g_info').removeClass('on')
      $('.product_info').css('display','none')
      $('.product_review').css('display','block')
    })
    $('.g_info').click(function(e){
      $(this).addClass('on')
      $('.g_review').removeClass('on')
      $('.product_info').css('display','block')
      $('.product_review').css('display','none')
    })
    
    //review

    $('.review_cb').click(function(){
      $(this).next().slideToggle();
    });



  
  
})
 
 
    
