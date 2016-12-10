$(function() {
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
        $.ajax({
            url: '/search',
            data: {
                json_str: $('form').serialize()
            },
            type: 'POST',
            success: function(response) {
                var data = $.parseJSON(response);

                $("#result").empty();

                $(data['places']).each(function() {
                    var $element = $template.clone().removeClass('template').appendTo('#result');
                    $element.find(".title-place").html(this.name);
                    $element.find(".desc-place").html(this.description);
                    $element.find(".address-place").html(this.location[0].address + " " + this.location[0].city);
                    $element.find(".rating-place").html(this.rate);
                    $element.find(".time-place").html(this.time[0].open + ' - ' + this.time[0].close);
                    $element.find(".check-place").attr('id', this.name);
                });

                $(".result").show();
                scrollToAnchor('search-engine-container');
            }
        });
    });


    //generate & show itinerary
    $("#link-itinerary").click(function() {
        var values = (function() {
            var a = [];

            $(".check-place:checked").each(function() {
                a.push(this.id);
            });

            return a;
        })();

        console.log(JSON.stringify(values));

        $.ajax({
            url: '/itinerary',
            data: {
                json_str: JSON.stringify(values)
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

                    if (this.type == 'recommendation') {
                        var $input = $("<button id='button-close-" + i + "'class='btn btn-danger' style='padding: 0px 5px;' type='button' onclick='removeRecommendation(" + i + ");'><span class='glyphicon glyphicon-remove' aria-hidden='true'></span></button>");
                        $input.appendTo($element.find(".itinerary-action"));
                    }
                });
            }
        });
    });

});

function sendTable() {
    var columns = ['time', 'location', 'address'];

    var tableObject = $('#itinerary-result tr').map(function(i) {
        var row = {};

        $(this).find('td').each(function(i) {
            if (i < 3) {
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
            location.reload();
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
