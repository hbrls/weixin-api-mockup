define(function (require) {
  var angular = require('angular');

  return {
    bootstrap: function (app) {
      angular.element(document).ready(function() {
        angular.bootstrap(document, [ app ]);
      });
    }
  };
});
