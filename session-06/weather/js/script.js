
$(document).ready(function() {

    let html = "";

    /* 
    * Weather data from Dark Sky API
    */

    $.getJSON('https://cors-anywhere.herokuapp.com/https://api.darksky.net/forecast/b48d97ffe4daa06874fa5ca5a3482b63/41.8262,-71.4030', function(data) {

        let currentTemp = data["currently"]["temperature"];
        let feelsTemp = data["currently"]["apparentTemperature"];
        let wind = data["currently"]["windSpeed"];
        $('#temp').text(currentTemp);
        $('#feels').text(feelsTemp);

       let fontWeight = Math.round(feelsTemp*10);// wght, 300 to 1000 — font weight
       console.log(fontWeight);

       let slant = 0;
       if (wind !== 0){
            slant = Math.round((wind/10)*-15);
       }
       console.log(slant);

       let setting = "'CASL' 1," + "'wght' " + fontWeight + ", 'slnt' " + slant;
       $('.highlight').css('font-variation-settings', setting);
       // slnt,  0 to -15  — Upright (0°) to Slanted (about 15°)
    });



    $.getJSON('emails.json', function(emails) {
       let html;
       $.each(emails, function( index, value ) {
          html += "<h2>" + value["Name"] + "</h2>";
       });
      $('main').append(html);
    });

});