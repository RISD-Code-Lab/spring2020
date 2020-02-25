// Script

var socket = io.connect('http://localhost:8080');

var player = {type: "player", x: 50, y: 90, dx: 0, dy: 0, w: 1.5, h: 1.5};
var game = [{type: "goal", x: 50, y: 10, w: 4, h: 4}];

const framerate = 30;
const increment = 0.05;
const indicators = true;


function create(object) {
    var element = $('<div>')
        .addClass(object.type)
        .css('top', object.y + 'vh')
        .css('left', object.x + 'vw')
        .css('width', object.w + 'vh')
        .css('height', object.h + 'vw')
        .css('transition-duration', (1000 / framerate) + 'ms');

    $('body').append(element).addClass('running')
}

function update(object) {
    // Update State with current dx
    object.x = object.x + object.dx;
    object.y = object.y + object.dy;

    // Optionally decay dx and dy?

    // Draw update
    $('.player')
        .css('top', object.y + 'vh')
        .css('left', object.x + 'vw');

    if (indicators) {
        var indicator = $('<div>')
            .addClass('indicator')
            .css('top', object.y + 'vh')
            .css('left', object.x + 'vw');

        $('body').append(indicator);
    }

}


function setup() {

    create(player);
    game.forEach(create);

}

function intersects(player, object) {
    var player_min_x = player.x - player.w / 2
    var player_max_x = player.x + player.w / 2
    var player_min_y = player.y - player.h / 2
    var player_max_y = player.y + player.h / 2

    var object_min_x = object.x - object.w / 2
    var object_max_x = object.x + object.w / 2
    var object_min_y = object.y - object.h / 2
    var object_max_y = object.y + object.h / 2

    var in_bounds_x =  player_min_x <= object_max_x && player_min_x >= object_min_x
                    || player_max_x <= object_max_x && player_max_x >= object_min_x

    var in_bounds_y = player_min_y <= object_max_y && player_min_y >= object_min_y
                   || player_max_y <= object_max_y && player_max_y >= object_min_y

    return in_bounds_x && in_bounds_y;
}

function check(player, game) {
    var finished = game.reduce(function(state, object) {
        return state || intersects(player, object)
    }, false);

    if (finished) {
        $('body').removeClass('running').addClass('done');
        console.log(player);
        console.log(game);
    }

}


function step(timestamp) {

    update(player);
    check(player, game);

    if ( $('body').hasClass('running') ) {
        window.setTimeout( function() {
            window.requestAnimationFrame(step);
        }, 1000 / framerate)
    }
}


$(document).ready(function() {

    setup();
    window.requestAnimationFrame(step);

    socket.on('update', function(data) {

        if (data.direction == 'U') {
            player.dy -= increment;
        }

        if (data.direction == 'R') {
            player.dx += increment;
        }

        if (data.direction == 'D') {
            player.dy += increment;
        }

        if (data.direction == 'L') {
            player.dx -= increment;
        }

    })

});
