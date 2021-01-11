$("form[name=patient").submit(function(e){

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/home/",
    type: "POST",
    success: function(resp) {
      window.location.href = "/patient-info/";
    }
    ,
    error: function(resp) {
      
    }
  });

  e.preventDefault();
});


$("form[name=doctor").submit(function(e){

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/home/",
    type: "POST",
    // data: data,
    // dataType: "json",
    success: function(resp) {
      window.location.href = "/data/";
    }
    ,
    error: function(resp) {
      
    }
  });

  e.preventDefault();
});

// $("form[name=info-form").submit(function(e){

//   var $form = $(this);
//   var $error = $form.find(".error");
//   $.ajax({
//     url: "/info/",
//     type: "POST",
//     success: function(resp) {
//       window.location.href = "/info/";
//     }
//     ,
//     error: function(resp) {
//       console.log(error)
//     }
//   });

//   e.preventDefault();
// });


// $("form[name=patient-list").submit(function(e){

//   var $form = $(this);
//   var $error = $form.find(".error");
//   $.ajax({
//     url: "/data/",
//     type: "POST",
//     success: function(resp) {
//       console.log(data)
//     }
//     ,
//     error: function(resp) {
      
//     }
//   });

//   e.preventDefault();
// });


$("form[name=patient-form").submit(function(e){


  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();
  // for (i = 0; i < 21; i++) {
  //   if (i < 10){
  //     alert('Please put your hand on sensor... Collecting data and submitting!!');
  //   }
  //   else if(i > 10){
  //     alert('Please put stethoscope on your left portion of chest for'+ 20-i +' sec!');
  //   }
  //   else{
  //     alert('Thanks!!  Your data has been saved !');
  //   }
    
  // //text += "The number is " + i + "<br>";
  // }
  // setTimeout(alert, 200, 'Please put your hand on sensor... Collecting data and submitting!!');
  // window.confirm('Please put your hand on sensor... Collecting data and submitting!!');
  // window.confirm('Please put stethoscope on your left portion of chest for 10 sec!'); 
  // setTimeout(alert, 3000, 'Please put stethoscope on your left portion of chest for 10 sec!');
  // window.confirm('Please wait... Saving information...Wait for the next alert');
  // window.confirm('Thanks!!  Your data has been saved !');
  // setTimeout(alert, 15000, 'Thanks!!!');

  
  $.ajax({
    url: "/send/",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      console.log(data)
      window.location.href = '/home/'
    }
    ,
    error: function(resp) {
      
    }
  });

  e.preventDefault();
  


  // window.setTimeout(window.location.href = '/home/', 20000);
  window.confirm('PRESS "OK" to Continue.....')
  window.confirm('Please put your 1 hand on temperature sensor and other on pulse sensor. PRESS "OK" to Continue');
  window.confirm('Please wait for 10 seconds.... and then PRESS "OK" to Continue.')
  window.confirm('Please put stethoscope on your left portion of chest for 10 seconds.... and then Press OK to continue...'); 
  window.confirm('Thanks!! Your data has been taken sucessfully !!!');

  window.location.href = '/home/';
});




// $("form[name=login_form").submit(function(e) {

//   var $form = $(this);
//   var $error = $form.find(".error");
//   var data = $form.serialize();

//   $.ajax({
//     url: "/user/login",
//     type: "POST",
//     data: data,
//     dataType: "json",
//     success: function(resp) {
//       window.location.href = "/dashboard/";
//     },
//     error: function(resp) {
//       $error.text(resp.responseJSON.error).removeClass("error--hidden");
//     }
//   });

//   e.preventDefault();
// });