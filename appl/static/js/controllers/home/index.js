define(function (require) {
  var $ = require('jquery');

  var angular = require('angular');

  angular
    .module('jd', [])
    .controller('HomeIndexCtrl', function ($scope, $http) {
      $scope.activity_stream = [];

      $http.get('/api/feeds').success(function (data) {
        $scope.activity_stream = data;
      });
    });

  var ab = require('angular-bootstrap');
  ab.bootstrap('jd');
});
