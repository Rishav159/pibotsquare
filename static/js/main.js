function buttonPressed(btn){
  $('#'+btn).addClass("active");
}
function buttonRelease(btn){
  $('#'+btn).removeClass("active");
}
function captureImage(){
  let link = document.createElement("a");
  let href = $('#currentImage').attr('src');
  let date = new Date();
  let fileName = date.toLocaleDateString().replace(new RegExp('/',"g"),'-')+'_'+date.toLocaleTimeString().replace(new RegExp(':',"g"),'-').replace(new RegExp(' ',"g"),'-')+'.png';
  link.setAttribute("href", href);
  link.setAttribute("download", fileName);
  $('#captured-image').html("");
  $('#captured-image').append(link);
  link.click();
}

$(document).ready(function(){
  //KeyPress Event
  $(document).keydown(function(e){
    let key = e.originalEvent.key;
    switch (key) {
      case 'ArrowUp':
      case 'w' : buttonPressed('forward-button'); break;
      case 'ArrowDown':
      case 's' : buttonPressed('back-button'); break;
      case 'ArrowLeft':
      case 'a' : buttonPressed('left-button'); break;
      case 'ArrowRight':
      case 'd' : buttonPressed('right-button'); break;
      case ' ': buttonPressed('capture-button'); break;
      default:
    }
  });
  //KeyRelease Event
  $(document).keyup(function(e){
    let key = e.originalEvent.key;
    switch (key) {
      case 'ArrowUp':
      case 'w' : buttonRelease('forward-button'); break;
      case 'ArrowDown':
      case 's' : buttonRelease('back-button'); break;
      case 'ArrowLeft':
      case 'a' : buttonRelease('left-button'); break;
      case 'ArrowRight':
      case 'd' : buttonRelease('right-button'); break;
      case ' ' :  buttonRelease('capture-button'); captureImage();break;
      default:
    }
  });
  //Scroll up events
  $(document).bind('DOMMouseScroll mousewheel',function(e){
    if(e.originalEvent.wheelDelta/120 > 0 || e.originalEvent.detail < 0){
      buttonPressed('camera-up');
      setTimeout(function(){
        buttonRelease('camera-up');
      },250);
    }else{
      buttonPressed('camera-down');
      setTimeout(function(){
        buttonRelease('camera-down');
      },250);
    }
  })

});
