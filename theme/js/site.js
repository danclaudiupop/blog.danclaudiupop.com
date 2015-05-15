$(document).ready(function() {

  // Variables
  var $nav = $('.navbar'),
      $body = $('body'),
      $window = $(window),
      navOffsetTop = $nav.offset().top-100,
      $document = $(document)

  function init() {
    $window.on('scroll', onScroll)
  }

  function onScroll() {
    if(navOffsetTop < $window.scrollTop() && !$body.hasClass('has-docked-nav')) {
      $body.addClass('has-docked-nav')
    }
    if(navOffsetTop > $window.scrollTop() && $body.hasClass('has-docked-nav')) {
      $body.removeClass('has-docked-nav')
    }
  }

  init();

});
