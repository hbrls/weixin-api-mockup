define(function (require) {
  var $ = require('jquery');
  require('bootstrap-datepicker-zh');

  $('.js-datepicker').datepicker({
    format: 'yyyy-mm-dd',
    language: 'zh-CN'
  });
});
