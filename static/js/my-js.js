$(function() {
    var start = "";
    var end = "";
    var data_place = "";

    $("#download-itinerary").click(function() {
        sendTable();
    });

    $(".subtagline__word").typed({
        strings: ["Jakarta, Bandung, Solo", "Palembang, Medan, Riau", "Lombok, Bali, Ambon"],
        typeSpeed: 150,
        loop: true
    });

    //suggestion
    $("#autocomplete").autocomplete({
            source:function(request, response) {
                $.getJSON('/autocomplete',{
                    q: request.term, // in flask, "q" will be the argument to look for using request.args
                }, function(data) {
                    response(data.matching_results); // matching_results from jsonify
                });
            },
            minLength: 2,
            select: function(event, ui) {
                console.log(ui.item.value); // not in your question, but might help later
        }
    });

    //show search result
    var $template = $('.template');
    $("#link").click(function() {
        $(".result").hide();
        
        // form validation
        var pesan = formValidate();
        if (pesan.length > 1) {
            $(".error").show();
            $(".error").html("<strong>Invalid input!</strong> " + pesan);
            return;
        }

        $.ajax({
            url: '/search',
            data: {
                json_str: $('form').serialize()
            },
            type: 'POST',
            success: function(response) {
                var data_all = $.parseJSON(response);
                data_place = JSON.stringify(data_all['data'])
                data_place_2 = data_all['data']
                start = data_all['open']
                end = data_all['close']

                $("#result").empty();
                $(".error").empty();
                $(data_place_2['places']).each(function() {
                    var $element = $template.clone().removeClass('template').appendTo('#result');
                    $element.find(".title-place").html(this.name);
                    $element.find(".desc-place").html(this.description);
                    $element.find(".address-place").html(this.location[0].address + " " + this.location[0].city);
                    $element.find(".rating-place").html(this.rate);
                    $element.find(".time-place").html(this.time[0].open + ' - ' + this.time[0].close);
                    $element.find(".check-place").attr('id', this.name);
                });
                if(data_place_2['places'].length != 0){
                    $(".result").show();
                }else{
                    $(".error").html("Your destination is not exist in our database :(");
                }

                scrollToAnchor('search-engine-container');
            }
        });
    });


    //generate & show itinerary
    $("#link-itinerary").click(function() {
        $('#myModal').modal();
        $("#loading").show();
        $(".modal-body").hide();        
        $(".modal-footer").hide();
        var values = (function() {
            var a = [];

            $(".check-place:checked").each(function() {
                a.push(this.id);
            });

            return a;
        })();

        //console.log(JSON.stringify(values));

        $.ajax({
            url: '/itinerary',
            data: {
                json_str: JSON.stringify(values), open: start, close : end, values: data_place
            },
            type: 'POST',
            success: function(response) {
                var data = $.parseJSON(response);
                var $itin_template = $('.itinerary-template');

                $("#itinerary-result").empty();
                $itin_template.clone().appendTo('#itinerary-result');

                var i = 0;
                $(data).each(function() {
                    i = i + 1;
                    var $element = $itin_template.clone().removeClass('itinerary-template').appendTo('#itinerary-result');
                    $element.attr('id', "itinerary-row-" + i);
                    $element.find(".itinerary-time").html(this.time);
                    $element.find(".itinerary-location").html(this.name);
                    $element.find(".itinerary-address").html(this.address);
                    $element.find(".itinerary-direction").html(this.direction);

                    if (this.type == 'recommendation') {
                        var $input = $("<button id='button-close-" + i + "'class='btn btn-danger' style='padding: 0px 5px;' type='button' onclick='removeRecommendation(" + i + ");'><span class='glyphicon glyphicon-remove' aria-hidden='true'></span></button>");
                        $input.appendTo($element.find(".itinerary-action"));
                    }
                });

                $(".modal-body").show();            
                $(".modal-footer").show();
                $("#loading").hide();
            }
        });
    });

});

function sendTable() {
    var columns = ['time', 'location', 'address', 'direction'];

    var tableObject = $('#itinerary-result tr').map(function(i) {
        var row = {};

        $(this).find('td').each(function(i) {
            if (i < 4) {
                var rowName = columns[i];
                row[rowName] = $(this).text();
            }
        });

        return row;
    }).get();

    tableObject.shift();
    console.log(JSON.stringify(tableObject));

    $.ajax({
        url: '/submit_itinerary',
        data: {
            json_str: JSON.stringify(tableObject)
        },
        type: 'POST',
        success: function(response) {
            console.log("waiting for download");
            window.open("http://ilhamfathy.me/itinerary.pdf",'_blank'); 
            //window.open("http://google.com",'_blank'); 


            setTimeout(function(){
             location.reload(); 
            }, 7000);
        }
    });
}

function scrollToAnchor(aid) {
    var aTag = $("div[name='" + aid + "']");
    $('html,body').animate({
        scrollTop: aTag.offset().top
    }, 'slow');
}

function removeRecommendation(aid) {
    $("#itinerary-row-" + aid).find(".itinerary-location").empty();
    $("#itinerary-row-" + aid).find(".itinerary-address").empty();
    $("#itinerary-row-" + aid).find(".itinerary-action").empty();
}

function formValidate() {
    var errorMsg = "";

    var iplace = $('input[name=place]').val();
    var icategories = $('input[name=categories]').val();
    var ifrom = $('input[name=from]').val();
    var iuntil = $('input[name=until]').val();

    if (iplace.length < 1) {
        errorMsg += " Where do you want to go?";
    }

    if (icategories.length < 1) {
        errorMsg += " What do you want to do?";
    }

    if (ifrom.length < 1 && iuntil.length < 1) {
        // use default time
        $('input[name=from').val("10:00");
        $('input[name=until]').val("17:00");
    } else if (ifrom.length < 1){
        errorMsg += " What time will you start your trip?";
    } else if (iuntil.length < 1) {
        errorMsg += " What time will you end your trip?";
    } else {
        // validate format
        var patt = /^[01][0-9]:[0-9][0-9]$|^2[0-3]:[0-9][0-9]$/i;
        var isvalid = patt.test(ifrom);
        isvalid &= patt.test(iuntil);
        isvalid &= (iuntil > ifrom);

        if (!isvalid) {
            errorMsg += " Invalid time or format";
        }
    }

    return errorMsg;
}
