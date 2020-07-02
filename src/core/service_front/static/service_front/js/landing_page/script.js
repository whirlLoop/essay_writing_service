$(document).ready(function(){
    $('.testimonial-slides').slick({
        dots: true,
        infinite: false,
        prevArrow: $('.prev-btn'),
        nextArrow: $('.next-btn'),
        speed: 500,
        fade: true,
        cssEase: 'linear'
    });
  });

  $('.prev-btn').click(function(){
    $('.testimonial-slides').slick('slickPrev');
  })

  $('.next-btn').click(function(){
    $('.testimonial-slides').slick('slickNext');
  })

const addPageBtn = document.getElementById("addPagesBtn");
const removePageBtn = document.getElementById("removePagesBtn");
const pagesInput = document.getElementById("pagesInput");
const totalWords = document.getElementById("totalWords");
var pages = pagesInput.value;

const addPages = value => {
    if (pages >= 100){
        pagesInput.value = pages;
        changeWordCount();
    }
    else{
        pages ++;
        pagesInput.value = pages;
        changeWordCount();
    }
}

const removePages = value => {
    if (pages <= 1){
        pagesInput.value = pages;
        changeWordCount();
    }
    else{
        pages --;
        pagesInput.value = pages;
        changeWordCount();
    }
}
addPageBtn.addEventListener("click", addPages);
removePageBtn.addEventListener("click", removePages);

const changeWordCount = () => {
    var totalWordCount = pages * 275;
    console.log(totalWordCount);
    totalWords.innerHTML = totalWordCount + " words";
}
