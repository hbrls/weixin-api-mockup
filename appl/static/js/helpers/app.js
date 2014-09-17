define(function () {
  var Probe = {};

  window.Probe = Probe;

  Probe.reload = function () {
    setTimeout(function (argument) {
      window.location = window.location;
    }, 500);
  };
});
