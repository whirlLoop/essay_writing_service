$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown(
        {
          'closeOnClick': false
        }
      );
    $('#close').on('click', function () {
      $('.sidenav').sidenav('close');
      $('.hidden').addClass('hidden');
     });
    $('select').formSelect();
    $('.datepicker').datepicker({
      defaultDate: new Date(),
      setDefaultDate: true,
      onSelect: time => setTimeRemaining(time),
      minDate: new Date(),
      autoClose: true,
    });
    $('.tooltipped').tooltip();
    $('.timepicker').timepicker({
      onSelect: (hrs, mins) => setFromNow(hrs, mins),
      autoClose: true,
      twelveHour: false
    });
  });

  function timeDiffCalc(dateFuture, dateNow) {
    let diffInMilliSeconds = Math.abs(dateFuture - dateNow) / 1000;

    // calculate days
    const days = Math.floor(diffInMilliSeconds / 86400);
    diffInMilliSeconds -= days * 86400;

    // calculate hours
    const hours = Math.floor(diffInMilliSeconds / 3600) % 24;
    diffInMilliSeconds -= hours * 3600;

    // calculate minutes
    const minutes = Math.floor(diffInMilliSeconds / 60) % 60;
    diffInMilliSeconds -= minutes * 60;

    let difference = '';
    if (days > 0) {
      difference += (days === 1) ? `${days} day, ` : `${days} days, `;
    }

    difference += (hours === 0 || hours === 1) ? `${hours} hour, ` : `${hours} hours `;

    difference += (minutes === 0 || hours === 1) ? `${minutes} minutes` : `${minutes} minutes`;

    return difference;
  }

var timeLeftInput = document.getElementById("timeLeft");

const setTimeRemaining = (dateSelected) => {
  const selectedDateInput = document.getElementById("deadline");
  const today = new Date();

  // const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
  // const diffDays = Math.round(Math.abs((firstDate - secondDate) / oneDay));
  
  if (dateSelected.toDateString() == today.toDateString()){
    console.log("its today alright")
    $("#timeRow").removeClass("hide")
  }else {
    $("#timeRow").addClass("hide");
    timeLeftInput.removeAttribute("style");
    var timeLeft = timeDiffCalc(dateSelected, today);
    timeLeftInput.innerHTML = timeLeft + " left";
  }
}

const setFromNow = (hours, minutes) => {
  // console.log(hours, minutes);
  timeLeftInput.innerHTML = `${hours} hrs` + ` ${minutes} mins` + " left";
  timeLeftInput.setAttribute("style", "color: red");
}

